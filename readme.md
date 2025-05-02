# Environment Setup Instructions

## Chrome Book
To activate the environment on your Chrome Book, use the following command:
```
source /home/hirram143/myenv/bin/activate
```

## iMac
To activate the environment on your iMac, use the following command:
```
source "/Users/aaran/Other Files/my_env_venv/bin/activate"
```

## Using the Environment in VS Code
1. Open VS Code.
2. Open the Command Palette (F1 or Ctrl+Shift+P).
3. Type `Python: Select Interpreter` and select it.
4. Choose the interpreter from the list that corresponds to your environment:
   - For Chrome Book: `/home/hirram143/myenv/bin/python`
   - For iMac: `/Users/aaran/Other Files/my_env_venv/bin/python`
5. Open a terminal in VS Code (Ctrl+`).
6. Activate the environment in the terminal:
   - For Chrome Book:
     ```
     source /home/hirram143/myenv/bin/activate
     ```
   - For iMac:
     ```
     source "/Users/aaran/Other Files/my_env_venv/bin/activate"
     ```

Now you can run your Python scripts within the activated environment in VS Code.
