# MC-265805: Executing a tail-recursive function consumes memory resources linearly with recursion depth

**Mojira URL:** [https://bugs.mojang.com/browse/MC-265805](https://bugs.mojang.com/browse/MC-265805)

## Report details

- **Mojira categories:** Commands; Performance
- **Project:** MC
- **Issue key:** MC-265805
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2023-10-13T03:04:30.169-0700
- **Updated:** 2025-03-25T12:25:59.617-0700
- **Resolution date:** 2023-10-30T02:25:17.279-0700
- **Affects versions:** 23w41a; 23w42a; 23w43a
- **Fix versions:** 23w44a
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 3
- **Attachment filenames:** crash-2023-10-13_18.43.29-server.txt; deobf_crash-2023-10-13_18.43.29-server.txt; mc-265805.zip

## Description

The bug
Before 23w41a, tail-recursive functions, which call themselves with /function at the end of their body, worked quite efficiently. They consume only a constant amount of memory resources regardless of the depth of the recursion.
Since 23w41a, however, even tail-recursive functions consume more memory resources for each recursive call.
How to reproduce
-

```
/gamerule maxCommandChainLength 2147483647
```

-

```
/function mc-265805:f
```
 → Eventually, the game crashes due to java.lang.OutOfMemoryError: Java heap space

data/mc-265805/functions/f.mcfunction

```
function mc-265805:f
```
Code analysis
net/minecraft/server/commands/FunctionCommand.java

```
public static <T extends ExecutionCommandSource<T>> void queueFunctions(
    Collection<CommandFunction<T>> functions,
    @Nullable CompoundTag arguments,
    T sender,
    T senderForExecution,
    ExecutionControl<T> control,
    FunctionCommand.Callbacks<T> callbacks
) throws CommandSyntaxException {
    CommandDispatcher<T> dispatcher = sender.dispatcher();
    MutableInt accumulatedReturnValue = new MutableInt();

    for(CommandFunction<T> function : functions) {
        ResourceLocation id = function.id();

        try {
            T listener = senderForExecution.clearCallbacks().withReturnValueConsumer(returnValue -> {
                int value = accumulatedReturnValue.addAndGet(returnValue);
                callbacks.signalResult(sender, id, value);
                sender.storeResults(true, value);
            });
            InstantiatedFunction<T> instantiatedFunction = function.instantiate(arguments, dispatcher, listener);
            control.queueNext(new CallFunction<>(instantiatedFunction).bind(listener));
        } catch (FunctionInstantiationException e) {
            throw ERROR_FUNCTION_INSTANTATION_FAILURE.create(id, e.messageComponent());
        }
    }
}
```
Because listener's return value consumer captures the original sender, JVM cannot release sender while listener is alive. In the case of recursive calls, a listener becomes the sender of another function call, chaining to the initial sender. Although calling a tail-recursive function still consumes only a constant amount of the command queue space, it now consumes a linear amount of memory resources due to the chain of execution command sources.
Heap dump analysis
Using VisualVM and a deobfuscated server.jar of 23w41a, a heap dump was obtained when the heap was almost full. According to the heap dump, the heap was almost fully occupied by the following three objects:
- net.minecraft.commands.CommandSourceStack: 30.6%

- net.minecraft.server.commands.FunctionCommand$$Lambda+0x000001c05ebefc78: 30.6%

- org.apache.commons.lang3.mutable.MutableInt: 30.6%

## Comments (1)

### Comment 1: migrated (2023-10-13T03:04:30.169-0700)

This comment contained multiple image attachments (3), please login to view the attachments.
