# LDOCE5 Viewer (PySide6, Python 3, Qt6)

-----

The LDOCE5 Viewer is an alternative dictionary viewer for the Longman Dictionary of Contemporary English 5th Edition (LDOCE 5).

![image](https://cloud.githubusercontent.com/assets/15828926/24585732/efb068a4-17bb-11e7-8294-7241f73d9ed8.png)

It runs on macOS (Intel, arm), Linux and Microsoft Windows.

This software is free and open source software licensed under the terms of GPLv3.

## How to Run

Follow these steps to set up and run the LDOCE5 Viewer:

1.  **Prerequisites:** Ensure you have Python 3.x installed on your system.

2.  **Clone the repository:**
    ```bash
    git clone https://github.com/pengyuanbin/ldoce5viewer.git
    ```
    (Note: Replace `https://github.com/pengyuanbin/ldoce5viewer.git` with the actual repository URL if different.)

3.  **Navigate to the project directory:**
    ```bash
    cd ldoce5viewer
    ```

4.  **Create and activate a Python virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

5.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

6.  **Precompile UI and resource files:**
    ```bash
    make precompile
    ```

7.  **Run the application:**
    ```bash
    venv/bin/python ldoce5viewer.py
    ```