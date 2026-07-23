import time
import functools
import sys

class DreamTracker:
    """Manages the state, depth, and time dilation of the recursive stack."""
    def __init__(self, time_multiplier=20):
        self.current_depth = 0
        self.time_multiplier = time_multiplier  # Each layer is 20x slower
        self.layer_names = ["Awake", "Layer 1: The Van", "Layer 2: The Hotel", "Layer 3: The Snow Fortress", "Limbo"]

    def get_layer_name(self, depth):
        if depth < len(self.layer_names):
            return self.layer_names[depth]
        return f"Limbo (Deep Layer {depth})"

# Initialize a global tracker instance
tracker = DreamTracker()

def dream_layer(func):
    """
    Decorator to track function execution layers, 
    calculating time dilation and visualizing the stack.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 1. Enter the deeper layer
        indent = "    " * tracker.current_depth
        layer_name = tracker.get_layer_name(tracker.current_depth)
        
        print(f"{indent}🌀 Entering [{layer_name}] (Depth: {tracker.current_depth})")
        print(f"{indent}   ↳ Executing: {func.__name__} with args: {args}")
        
        start_real_time = time.time()
        tracker.current_depth += 1
        
        try:
            # 2. Execute the actual function code
            result = func(*args, **kwargs)
            return result
            
        except Exception as e:
            # Catching a "Kick" or error to collapse the stack safely
            print(f"{indent}💥 [KICK RECEIVED] Collapsing layer due to: {str(e)}")
            raise e
            
        finally:
            # 3. Exit the layer and calculate time dilation
            tracker.current_depth -= 1
            end_real_time = time.time()
            
            real_duration = end_real_time - start_real_time
            # Formula: Simulated Time = Real Time * (Multiplier ^ Depth)
            dilated_duration = real_duration * (tracker.time_multiplier ** tracker.current_depth)
            
            print(f"{indent}⏰ Exiting [{layer_name}]")
            print(f"{indent}   ↳ Real Time: {real_duration:.6f}s | Dilated Dream Time: {dilated_duration:.2f}s")
            
    return wrapper

# --- Example Usage: Recursive Fibonacci with Inception Physics ---

@dream_layer
def search_subconscious(target_depth, current=0):
    """A recursive function simulating descending into deeper dream states."""
    # Artificial pause to simulate real work being done in the layer
    time.sleep(0.05) 
    
    if current == target_depth:
        print("    " * current + "🎯 Target memory found in the subconscious!")
        return True
        
    # Guard rail / Totem check: Prevent falling too deep into Limbo
    if current >= 4:
        raise RuntimeError("Lost stability! Dropping out of reality!")
        
    # Descend to the next layer
    return search_subconscious(target_depth, current + 1)

if __name__ == "__main__":
    print("=== INITIALIZING INCEPTION PROTOCOL ===")
    
    print("\n--- Mission 1: Successful Extraction (3 Layers Deep) ---")
    search_subconscious(3)
    
    print("\n--- Mission 2: Falling into Limbo (Triggers a Kick) ---")
    try:
        search_subconscious(5)
    except RuntimeError:
        print("\n=== SYSTEM RESET: Back to Reality ===")