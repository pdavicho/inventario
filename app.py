import streamlit as st
import pandas as pd
from PIL import Image

df = pd.read_csv('INVENTARIO.csv')

imagen = Image.open('acerosNegrete.png')
st.sidebar.image(imagen)
st.title('Sistema de Inventario')
opcion = st.sidebar.selectbox('Seleccione una opción', ['Ver inventario', 'Agregar producto', 'Entrada producto', 'Salida producto', 'Editar'])

if opcion == 'Ver inventario':
    st.table(df)

elif opcion == 'Agregar producto':
    codigo_producto = st.text_input('Codigo del Producto:')
    descripcion = st.text_input('Descripcion:')
    eIniciales = st.number_input('Existencias Iniciales:', min_value=0)
    entradas = st.number_input('Entrada:', min_value=0)
    salidas = st.number_input('Salidas', min_value=0)

    if st.button('Agregar'):
        df = df.append({'Codigo': codigo_producto, 'Descripcion': descripcion, 'Iniciales': eIniciales, 'Entradas': entradas, 'Salidas': salidas}, ignore_index=True)
        df.to_csv('INVENTARIO.csv', index=False)
        st.success('Producto agregado correctamente')

elif opcion == 'Entrada producto':
    codigoProducto = st.text_input('Ingrese el nombre del producto que desea editar')
    fila = df.loc[df['Codigo'] == codigoProducto]
    if not fila.empty:
        entrada1 = fila['Entradas'].values[0]
        nuevaEntrada = st.number_input('Entrada:', min_value=0)
        entradaTotal = entrada1 + nuevaEntrada
        if st.button('Guardar Cambios'):
            df.loc[df['Codigo'] == codigoProducto, ['Entradas']] = [entradaTotal]
            df.loc[df['Codigo'] == codigoProducto, ['Stock']] = df['Iniciales'] + df['Entradas'] - df['Salidas']
            df.to_csv('INVENTARIO.csv', index=False)
            st.success('Entrada agregada correctamente')

elif opcion == 'Salida producto':
    codigoProducto = st.text_input('Ingrese el nombre del producto que desea editar')
    fila = df.loc[df['Codigo'] == codigoProducto]
    if not fila.empty:
        salida1 = value=fila['Salidas'].values[0]
        nuevaSalida = st.number_input('Salida:', min_value=0)
        salidaTotal = salida1 + nuevaSalida
        if st.button('Guardar Cambios'):
            df.loc[df['Codigo'] == codigoProducto, ['Salidas']] = [salidaTotal]
            df.loc[df['Codigo'] == codigoProducto, ['Stock']] = df['Iniciales'] + df['Entradas'] - df['Salidas']
            df.to_csv('INVENTARIO.csv', index=False)
            st.success('Salida agregada correctamente')

elif opcion == 'Editar':
    edited_df = st.experimental_data_editor(df)
    if edited_df is not None:
        df = edited_df
        #st.success('Los datos se han actualizado correctamente')

    if st.button('GUARDAR'):
        df.to_csv('INVENTARIO.csv', index=False)
        st.success('Excel editado correctamente')
        st.balloons()



        




