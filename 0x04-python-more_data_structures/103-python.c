#include <Python.h>

/**
 * print_python_bytes - prints basic info from C about Python lists
 * @p: PyObject representing list
 */
void print_python_bytes(PyObject *p)
{
	unsigned char size, i = 0;
	PyBytesObject *str = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", str->ob_sval);
	if (((PyVarObject *)p)->ob_size > 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;
			printf("  first %d bytes:", size);
	while (i < size)
	{
		printf(" %02hhx", str->ob_sval[i]);
		if (i == (size - 1))
			printf("\n");
		else
			printf(" ");
		i++;
	}
}

/**
 * print_python_list - prints basic info from C about Python lists
 * @p: PyObject representing list
 */
void print_python_list(PyObject *p)
{
	int size = var->ob_size;
	int i = 0;
	const char *str;
	PyListObject *list = (PyListObject *)p;
	PyVarObjest *var = (PyVarObjest *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", list->allocated);

	while (i < size)
	{
		str = (list->ob_item[i])->ob_type->tp_name;
		printf("Element %d: %s\n", i, str);
		if (!strcmp(str, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
		i++;
	}
}
