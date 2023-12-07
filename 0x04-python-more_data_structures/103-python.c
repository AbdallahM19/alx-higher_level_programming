#include <Python.h>

/**
 * print_python_bytes - prints basic info from C about Python lists
 * @p: PyObject representing list
 */
void print_python_bytes(PyObject *p)
{
	int size, i = 0;
	char *str = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	PyBytes_AsStringAndSize(p, &str, &size);
	printf("  size: %li\n", size);
	printf("  trying string: %s\n", str);
	if (size < 10)
		printf("  first %li bytes:", size + 1);
	else
		printf("  first 10 bytes:");
	while (i < size && i < 10)
	{
		printf(" %02hhx", str[i]);
		i++;
	}
	printf("\n");
}

/**
 * print_python_list - prints basic info from C about Python lists
 * @p: PyObject representing list
 */
void print_python_list(PyObject *p)
{
	int size = PyList_Size(p);
	const char *str;
	int i = 0;
	PyListObject *list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %li\n", list->allocated);

	while (i < size)
	{
		str = (list->ob_item[i])->ob_type->tp_name;
		printf("Element %d: %s\n", i, str);
		if (!strcmp(str, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
		i++;
	}
}
