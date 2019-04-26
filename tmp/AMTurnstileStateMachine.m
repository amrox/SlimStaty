#import "AMTurnstileStateMachine.h"


@interface AMTurnstileStateMachine ()
@property (readwrite) AMTurnstileStateMachineState state;
@end


@implementation AMTurnstileStateMachine

- (instancetype)init
{
    self = [super init];
    if (self) {
        // TODO: set initial state?
        // _state = 0;
    }
    return self;
}

- (instancetype)initWithState:(AMTurnstileStateMachineState)state
{
    self = [super init];
    if (self) {
        _state = state;
    }
    return self;
}

- (AMTurnstileStateMachineState)fire:(AMTurnstileStateMachineEvent)event error:(NSError *_Nullable *_Nullable)outError
{
    /* coin: locked -> unlocked */
    if (event == AMTurnstileStateMachineEventCoin && self.state == AMTurnstileStateMachineStateLocked) {
        return [self _transitionToState:AMTurnstileStateMachineStateUnlocked];
    }
    /* push: unlocked -> locked */
    if (event == AMTurnstileStateMachineEventPush && self.state == AMTurnstileStateMachineStateUnlocked) {
        return [self _transitionToState:AMTurnstileStateMachineStateLocked];
    }
    if (outError != NULL) {
        // TODO: better error
        *outError = [[NSError alloc] initWithDomain:@"co.mrox" code:1 userInfo:nil];
    }

    return self.state;
}

- (AMTurnstileStateMachineState)_transitionToState:(AMTurnstileStateMachineState)state
{
    [self.delegate turnstileStateMachine:self willTransitionToState:state];
    self.state = state;
    [self.delegate turnstileStateMachine:self didTransitionToState:state];
    return self.state;
}


@end
