#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - prints basic info from C about Python lists
 * @p: PyObject representing list
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t allocated = ((PyListObject *)p)->allocated;
    Py_ssize_t i;
    PyObject *type;

    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", allocated);

    for (i = 0; i < size; i++)
    {
        type = PyList_GetItem(p, i);
        printf("Element %zd: %s\n", i, Py_TYPE(type)->tp_name);
    }
}

void print_python_bytes(PyObject *p)
{
    printf("[.] bytes object info\n");

    if (PyBytes_Check(p))
    {
        Py_ssize_t size = PyBytes_Size(p);
        char *str = PyBytes_AsString(p);

        printf("  size: %ld\n", size);
        printf("  trying string: %s\n", str ? str : "(error)");

        printf("  first 10 bytes:");
        for (Py_ssize_t i = 0; i < 10 && i < size; ++i)
            printf(" %02x", (unsigned char)str[i]);
        printf("\n");
    }
    else
    {
        printf("  [ERROR] Invalid Bytes Object\n");
    }
}
