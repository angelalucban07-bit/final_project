# Typing Speed and Accuracy Test

A Python-based Typing Speed and Accuracy Test application built using Tkinter. This project allows users to select different paragraphs and measure their typing performance through typing speed (WPM), accuracy, and total time.

### Project Origin
* **Original Project Reference:** https://github.com/SunnyVachhetA/Typing-Speed-Test
* https://www.youtube.com/watch?v=jbtOCcj1AXk
* *Note: The original project was structurally enhanced to fully implement Object Oriented Programming.*

> [!NOTE]
> **Disclaimer:** This repository is modified and maintained solely as a submission for my **Final Project**. 

## Features

- Multiple typing paragraphs
- Paragraph navigation
- Real-time timer
- Words Per Minute (WPM) calculation
- Accuracy calculation
- Color indication for correct and incorrect typing
- Prevention of copy, paste, and right-click
- Result page displaying:
  - Accuracy
  - WPM
  - Total Time
- Graphical User Interface using Tkinter

## OOP Concepts Implemented

### Inheritance

```
BaseWindow
    ↑
Timer
    ↑
Statistics
    ↑
TypingUI
    ↑
TypingTest
```

Abstract class implementation:

```
TypingFeature (ABC)
        ↑
TypingTest
```

### Encapsulation

The following variables are encapsulated:

```python
self._start_flag
self._backspace_count
self._key_press_count
self._get_user_text
```

### Abstraction

Implemented using an abstract class:

```python
TypingFeature(ABC)
```

which defines:

- `reset_data()`
- `back_to_home()`

and is implemented by:

```python
TypingTest
```

### Polymorphism

Method overriding is implemented through:

```python
BaseWindow.get_exit()
```

which is overridden in:

```python
TypingTest.get_exit()
```

to provide an exit confirmation dialog.

## Project Structure

```
Typing-Speed-Test/
│
├── main.py
├── base_window.py
├── timer.py
├── statistics.py
├── typing_ui.py
├── typing_feature.py
├── paragraph_text.py
└── README.md
```

## Technologies Used

- Python 3
- Tkinter

## Reference

This project was inspired by and based on the following repository:

**SunnyVachhetA - Typing-Speed-Test**

https://github.com/SunnyVachhetA/Typing-Speed-Test

The original project was studied and further refactored to implement:

- Inheritance
- Encapsulation
- Abstraction
- Polymorphism
- Improved code readability

