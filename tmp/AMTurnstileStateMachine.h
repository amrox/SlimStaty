

// TODO: generated header
#import <Foundation/Foundation.h>


typedef NS_ENUM(NSUInteger, AMTurnstileStateMachineState) {
    AMTurnstileStateMachineStateLocked,
    AMTurnstileStateMachineStateUnlocked,
} NS_SWIFT_NAME(TurnstileStateMachine.State);


typedef NS_ENUM(NSUInteger, AMTurnstileStateMachineEvent) {
    AMTurnstileStateMachineEventPush,
    AMTurnstileStateMachineEventCoin,
} NS_SWIFT_NAME(TurnstileStateMachine.Event);

@protocol AMTurnstileStateMachineDelegate;


NS_ASSUME_NONNULL_BEGIN

NS_SWIFT_NAME(TurnstileStateMachine)
@interface AMTurnstileStateMachine : NSObject

@property (readonly) AMTurnstileStateMachineState state;

@property (nonatomic, weak, nullable) id<AMTurnstileStateMachineDelegate> delegate;

- (instancetype)init NS_DESIGNATED_INITIALIZER;
- (instancetype)initWithState:(AMTurnstileStateMachineState)state NS_DESIGNATED_INITIALIZER;

- (AMTurnstileStateMachineState)fire:(AMTurnstileStateMachineEvent)event error:(NSError *_Nullable *_Nullable)outError;

@end


NS_SWIFT_NAME(TurnstileStateMachineDelegate)
@protocol AMTurnstileStateMachineDelegate <NSObject>

- (void)turnstileStateMachine:(AMTurnstileStateMachine *)stateMachine willTransitionToState:(AMTurnstileStateMachineState)state;
- (void)turnstileStateMachine:(AMTurnstileStateMachine *)stateMachine didTransitionToState:(AMTurnstileStateMachineState)state;

@end

NS_ASSUME_NONNULL_END
