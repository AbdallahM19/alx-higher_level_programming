#include <Python.h>

/**
 * print_python_bytes - prints basic info from C about Python bytes objects
 * @p: PyObject representing bytes
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    unsigned char *str;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    str = (unsigned char *)PyBytes_AsString(p);

    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", str);
    
    printf("  first %zd bytes:", size < 10 ? size : 10);
    for (i = 0; i < size && i < 10; ++i)
        printf(" %02x", str[i]);
    printf("\n");
}

/**
 * print_python_list - prints basic info from C about Python lists
 * @p: PyObject representing list
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;
    const char *str;
    PyListObject *list = (PyListObject *)p;

    printf("[*] Python list info\n");

    size = PyList_Size(p);

    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", ((PyVarObject *)p)->ob_size);

    for (i = 0; i < size; ++i)
    {
        str = (list->ob_item[i])->ob_type->tp_name;
        printf("Element %zd: %s\n", i, str);

        if (strcmp(str, "bytes") == 0)
            print_python_bytes(list->ob_item[i]);
    }
}

