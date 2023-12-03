#include <Python.h>

/**
 * print_python_list_info - prints basic info from C about Python lists
 * @p: PyObject representing list
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;
	int size = PyList_Size(p);
	int i = 0;
	PyObject *type;

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);

	while (i < size)
	{
		type = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(type)->tp_name);
		i++;
	}
}
