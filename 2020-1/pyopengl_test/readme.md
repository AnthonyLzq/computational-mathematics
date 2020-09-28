# Testing PyOpenGL

## Prerequisites

This project is currently using `Python 3.8.3` and `pip 20.0.2`.

Clone this project and run the following commands in your terminal:

1. To setup a `Python` virtual environment:
    ```console
    $ python -m venv venv
    ```

2. Use the activate the `Python` virtual environment:
    ```console
    $ source venv/bin/activate
    ```

3. To install the requirements:
    ```console
    $ pip install -r requirements.txt
    ```
    Be aware of what is your `pip` version.

3. To give execute permissions to the `main.sh` file:
    ```console
    $ chmod u+x main.sh
    ```

## Usage

Once you have done the three steps shown above, run the following command in your terminal:

```console
$ ./main.sh
```

To control which axis the rotation is made on, change the parameters in the `glRotatef()` function, located in the `/src/controllers/window.py` file, in the method `_triangle_easy_operations`.

- To rotate the triangle around the X axis, use:
  `glRotatef(1, 1, 0, 0)`

- To rotate the triangle around the Y axis, use:
  `glRotatef(1, 0, 1, 0)`

- To rotate the triangle around the Z axis, use:
  `glRotatef(1, 0, 0, 1)`

After finish the test you could make, please run the following command in your terminal:

```console
$ deactivate
```

This will deactivate the `Python` virtual environment, so you will be able to use your global environment as usual.

## Author
-   **Anthony Luzquiños** - _Initial Work_ - _Documentation_ - [AnthonyLzq](https://github.com/AnthonyLzq).