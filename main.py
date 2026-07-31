from scraper import obtener_productos


def main():

    print("================================")
    print(" Track Monitor iniciado")
    print("================================")

    productos = obtener_productos()

    print(f"\nProductos encontrados: {len(productos)}")

    for producto in productos:
        print("----------------------------")
        print(f"Nombre : {producto.get('nombre')}")
        print(f"Precio : {producto.get('precio')}")
        print(f"Estado : {producto.get('estado')}")


if __name__ == "__main__":
    main()
