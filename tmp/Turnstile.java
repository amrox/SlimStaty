package hi;

import java.util.HashSet;
import java.util.Set;

public class TurnstileStateMachine {

    public enum State {
        LOCKED,
        UNLOCKED,
    }

    public enum Event {
        PUSH,
        COIN,
    }

    public static class Exception extends java.lang.Exception {}

    public interface OnStateChangeListener {
        void onStateWillChange(TurnstileStateMachine stateMachine, TurnstileStateMachine.State newState);
        void onStateDidChange(TurnstileStateMachine stateMachine, TurnstileStateMachine.State newState);
    }

    public TurnstileStateMachine() {
    }

    public TurnstileStateMachine(State state) {
        this.state = state;
    }

    public State getState() {
        return state;
    }

    public synchronized State fire(Event event) throws Exception {
        
        /* coin: locked -> unlocked */
        if (event == Event.COIN && this.state == State.LOCKED) {
            return transition(State.UNLOCKED);
        }
        
        /* push: unlocked -> locked */
        if (event == Event.PUSH && this.state == State.UNLOCKED) {
            return transition(State.LOCKED);
        }
        
        throw new Exception();
    }

    private State transition(State state) {
        for (OnStateChangeListener l: listeners) {
            if (l != null) {
                l.onStateWillChange(this, state);
            }
        }
        this.state = state;
        for (OnStateChangeListener l: listeners) {
            if (l != null) {
                l.onStateDidChange(this, state);
            }
        }
        return this.state;
    }

    public synchronized void addListener(OnStateChangeListener listener) {
        listeners.add(listener);
    }

    public synchronized void removeListener(OnStateChangeListener listener) {
        listeners.remove(listener);
    }

    private State state = State.LOCKED;
    private Set<OnStateChangeListener> listeners = new HashSet<>();
}