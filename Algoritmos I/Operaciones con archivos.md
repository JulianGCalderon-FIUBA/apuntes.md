## Lectura de Archivos

```c
int leidos = fscanf(stream, formato, punteros);

//Hay distintas alternativas para la condicion del ciclo
while (leidos != EOF)
			(leidos == nro) //nro: Cantidad de punteros
{
    // Procesar
		leidos = fscanf(stream, formato, punteros);
}
```

```c
size_t leidos = fread(&buffer, sizeof(buffer), nro, stream);

//Hay distintas alternativas para la condicion del ciclo
while (leidos != 0)
			(leidos == nro)
{
		// Procesar
		leidos = fread(&buffer, sizeof(buffer), nro, stream);
}
```

## Operaciones Avanzadas

### Mezcla

```c
FILE *stream_1 = fopen("archivo_1", "r");
FILE *stream_2 = fopen("archivo_2", "r");
FILE *mezcla = fopen("mezcla", "w");

buffer_t buffer_1;
buffer_t buffer_2;

size_t leidos_1 = fread(&buffer_1, sizeof(buffer_t), 1, stream_1);
size_t leidos_2 = fread(&buffer_2, sizeof(buffer_t), 1, stream_2);

while (leidos_1 == 1 && leidos_2 == 1)
{
		if (buffer_1.clave <= buffer_2.clave)
		{
				fwrite(&buffer_1, sizeof(buffer_t), 1, mezcla);
				leidos_1 = fread(&buffer_1, sizeof(buffer), 1, stream_1);
		} 
		else
		{
				fwrite(&buffer_2, sizeof(buffer_t), 1, mezcla);
				leidos_2 = fread(&buffer_2, sizeof(buffer), 1, stream_2);
		}
}

while (leidos_1 == 1)
{
		fwrite(&buffer_1, sizeof(buffer_t), 1, mezcla);
		leidos_1 = fread(&buffer_1, sizeof(buffer), 1, stream_1);
}

while (leidos_2 == 1)
{
		fwrite(&buffer_2, sizeof(buffer_t), 1, mezcla);
		leidos_2 = fread(&buffer_2, sizeof(buffer), 1, stream_2);
}

```

### Unión

```c
FILE *stream_1 = fopen("archivo_1", "r");
FILE *stream_2 = fopen("archivo_2", "r");
FILE *union= fopen("union", "w");

buffer_t buffer_1;
buffer_t buffer_2;

size_t leidos_1 = fread(&buffer_1, sizeof(buffer_t), 1, stream_1);
size_t leidos_2 = fread(&buffer_2, sizeof(buffer_t), 1, stream_2);

while (leidos_1 == 1 && leidos_2 == 1)
{
		if (buffer_1.clave < buffer_2.clave)
		{
				fwrite(&buffer_1, sizeof(buffer_t), 1, union);
				leidos_1 = fread(&buffer_1, sizeof(buffer), 1, stream_1);
		} 
		else if (buffer_1.clave > buffer_2.clave)
		{ 
				fwrite(&buffer_2, sizeof(buffer_t), 1, union);
				leidos_2 = fread(&buffer_2, sizeof(buffer), 1, stream_2);
		}
		else
		{
				fwrite(&buffer_1, sizeof(buffer_t), 1, union);
				leidos_1 = fread(&buffer_1, sizeof(buffer), 1, stream_1);
				leidos_2 = fread(&buffer_2, sizeof(buffer), 1, stream_2);
		}
}

while (leidos_1 == 1)
{
		fwrite(&buffer_1, sizeof(buffer_t), 1, union);
		leidos_1 = fread(&buffer_1, sizeof(buffer), 1, stream_1);
}

while (leidos_2 == 1)
{
		fwrite(&buffer_2, sizeof(buffer_t), 1, union);
		leidos_2 = fread(&buffer_2, sizeof(buffer), 1, stream_2);
}
```

### Intersección

```c
FILE *stream_1 = fopen("archivo_1", "r");
FILE *stream_2 = fopen("archivo_2", "r");
FILE *intersec= fopen("intersec", "w");

buffer_t buffer_1;
buffer_t buffer_2;

size_t leidos_1 = fread(&buffer_1, sizeof(buffer_t), 1, stream_1);
size_t leidos_2 = fread(&buffer_2, sizeof(buffer_t), 1, stream_2);

while (leidos_1 == 1 && leidos_2 == 1)
{
		if (buffer_1.clave < buffer_2.clave)
		{
				leidos_1 = fread(&buffer_1, sizeof(buffer), 1, stream_1);
		} 
		else if (buffer_1.clave > buffer_2.clave)
		{ 
				leidos_2 = fread(&buffer_2, sizeof(buffer), 1, stream_2);
		}
		else
		{
				fwrite(&buffer_1, sizeof(buffer_t), 1, intersec);
				leidos_1 = fread(&buffer_1, sizeof(buffer), 1, stream_1);
				leidos_2 = fread(&buffer_2, sizeof(buffer), 1, stream_2);
		}
}
```

### Diferencia

```c
FILE *stream_1 = fopen("archivo_1", "r");
FILE *stream_2 = fopen("archivo_2", "r");
FILE *diferencia= fopen("diferencia", "w");

buffer_t buffer_1;
buffer_t buffer_2;

size_t leidos_1 = fread(&buffer_1, sizeof(buffer_t), 1, stream_1);
size_t leidos_2 = fread(&buffer_2, sizeof(buffer_t), 1, stream_2);

while (leidos_1 == 1 && leidos_2 == 1)
{
		if (buffer_1.clave < buffer_2.clave)
		{
				fwrite(&buffer_1, sizeof(buffer_t), 1, diferencia);
				leidos_1 = fread(&buffer_1, sizeof(buffer), 1, stream_1);
		} 
		else if (buffer_1.clave > buffer_2.clave)
		{ 
				leidos_2 = fread(&buffer_2, sizeof(buffer), 1, stream_2);
		}
		else
		{
				leidos_1 = fread(&buffer_1, sizeof(buffer), 1, stream_1);
				leidos_2 = fread(&buffer_2, sizeof(buffer), 1, stream_2);
		}
}

while (leidos_1 == 1)
{
		fwrite(&buffer_1, sizeof(buffer_t), 1, diferencia);
		leidos_1 = fread(&buffer_1, sizeof(buffer), 1, stream_1);
}
```
