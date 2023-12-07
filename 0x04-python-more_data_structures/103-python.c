#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p)
{
    long int size = PyList_Size(p);
    int i;
    PyListObject *list = (PyListObject *)p;
    const char *type;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %li\n", size);
    printf("[*] Allocated = %li\n", list->allocated);

    for (i = 0; i < size; i++)
    {
        type = (list->ob_item[i])->ob_type->tp_name;
        printf("Element %i: %s\n", i, type);

        if (!strcmp(type, "bytes"))
            print_python_bytes(list->ob_item[i]);
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

