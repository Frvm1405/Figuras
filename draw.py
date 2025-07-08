import cv2
import numpy as np

class ImageDrawer:
    def __init__(self, image_path):
        """Initialize the class by loading the image from the given path.
        Args:
            image_path (str): Path to the image file.
        Raises:
            ValueError: If the image cannot be loaded.
        """
        self.image = cv2.imread(image_path)
        if self.image is None:
            raise ValueError("No se pudo cargar la imagen. Verifica la ruta.")
        self.original_image = self.image.copy()
        self.color = (0, 255, 0)  # Default color: green (BGR)
        self.thickness = 2        # Default thickness

    def reset_image(self):
        """Restore the image to its original state."""
        self.image = self.original_image.copy()

    def draw_rectangle(self):
        """Interactively draw a rectangle on the image using the mouse.
        - Click and drag to draw.
        - Press Enter to confirm, ESC to cancel.
        """
        print("\nDibujar Rectángulo: clic y arrastra, Enter para confirmar, ESC para cancelar")
        temp_img = self.image.copy()
        rect = [0, 0, 0, 0]
        drawing = False

        def mouse_callback(event, x, y, flags, param):
            nonlocal rect, drawing, temp_img
            if event == cv2.EVENT_LBUTTONDOWN:
                rect = [x, y, x, y]
                drawing = True
            elif event == cv2.EVENT_MOUSEMOVE and drawing:
                rect[2], rect[3] = x, y
                temp = self.image.copy()
                cv2.rectangle(temp, (rect[0], rect[1]), (rect[2], rect[3]), self.color, self.thickness)
                temp_img = temp
                cv2.imshow("Dibujar Rectángulo", temp_img)
            elif event == cv2.EVENT_LBUTTONUP and drawing:
                rect[2], rect[3] = x, y
                drawing = False

        cv2.namedWindow("Dibujar Rectángulo")
        cv2.setMouseCallback("Dibujar Rectángulo", mouse_callback)
        cv2.imshow("Dibujar Rectángulo", self.image)

        while True:
            cv2.imshow("Dibujar Rectángulo", temp_img)
            key = cv2.waitKey(1) & 0xFF
            if key == 13:  # Enter
                self.image = temp_img.copy()
                cv2.destroyWindow("Dibujar Rectángulo")
                print(f"Rectángulo dibujado en: ({rect[0]}, {rect[1]}) a ({rect[2]}, {rect[3]})")
                break
            elif key == 27:  # ESC
                cv2.destroyWindow("Dibujar Rectángulo")
                print("Operación cancelada")
                break

    def draw_line(self):
        """Interactively draw a line on the image using the mouse.
        - Click two points to define the line.
        - Press Enter to confirm, ESC to cancel.
        """
        print("\nDibujar Línea: clic en dos puntos, Enter para confirmar, ESC para cancelar")
        temp_img = self.image.copy()
        points = []

        def mouse_callback(event, x, y, flags, param):
            nonlocal points, temp_img
            if event == cv2.EVENT_LBUTTONDOWN and len(points) < 2:
                points.append((x, y))
                temp = self.image.copy()
                if len(points) == 1:
                    cv2.circle(temp, points[0], 3, self.color, -1)
                elif len(points) == 2:
                    cv2.line(temp, points[0], points[1], self.color, self.thickness)
                temp_img = temp
                cv2.imshow("Dibujar Línea", temp_img)

        cv2.namedWindow("Dibujar Línea")
        cv2.setMouseCallback("Dibujar Línea", mouse_callback)
        cv2.imshow("Dibujar Línea", self.image)

        while True:
            cv2.imshow("Dibujar Línea", temp_img)
            key = cv2.waitKey(1) & 0xFF
            if key == 13 and len(points) == 2:  # Enter
                self.image = temp_img.copy()
                cv2.destroyWindow("Dibujar Línea")
                print(f"Línea dibujada de {points[0]} a {points[1]}")
                break
            elif key == 27:  # ESC
                cv2.destroyWindow("Dibujar Línea")
                print("Operación cancelada")
                break

    def draw_circle(self):
        """Interactively draw a circle on the image using the mouse.
        - Click to set the center, drag to set the radius.
        - Press Enter to confirm, ESC to cancel.
        """
        print("\nDibujar Círculo: clic para centro y arrastra, Enter para confirmar, ESC para cancelar")
        temp_img = self.image.copy()
        center = None
        radius = 0
        drawing = False

        def mouse_callback(event, x, y, flags, param):
            nonlocal center, radius, drawing, temp_img
            if event == cv2.EVENT_LBUTTONDOWN:
                center = (x, y)
                radius = 0
                drawing = True
            elif event == cv2.EVENT_MOUSEMOVE and drawing:
                radius = int(np.hypot(x - center[0], y - center[1]))
                temp = self.image.copy()
                cv2.circle(temp, center, radius, self.color, self.thickness)
                temp_img = temp
                cv2.imshow("Dibujar Círculo", temp_img)
            elif event == cv2.EVENT_LBUTTONUP and drawing:
                radius = int(np.hypot(x - center[0], y - center[1]))
                drawing = False

        cv2.namedWindow("Dibujar Círculo")
        cv2.setMouseCallback("Dibujar Círculo", mouse_callback)
        cv2.imshow("Dibujar Círculo", self.image)

        while True:
            cv2.imshow("Dibujar Círculo", temp_img)
            key = cv2.waitKey(1) & 0xFF
            if key == 13 and center and radius > 0:  # Enter
                self.image = temp_img.copy()
                cv2.destroyWindow("Dibujar Círculo")
                print(f"Círculo dibujado en {center} con radio {radius}")
                break
            elif key == 27:  # ESC
                cv2.destroyWindow("Dibujar Círculo")
                print("Operación cancelada")
                break

    def show_image(self):
        """Display the current image in a window."""
        cv2.imshow("Imagen Actual", self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def save_image(self):
        """Save the current image to a file specified by the user."""
        filename = input("Ingrese el nombre del archivo para guardar (ej. resultado.jpg): ")
        if not filename.strip():
            print("Nombre de archivo vacío. Imagen no guardada.")
            return
        cv2.imwrite(filename, self.image)
        print(f"Imagen guardada como {filename}")

    def menu(self):
        """Show the main menu and handle user input for drawing and image operations."""
        while True:
            print("\n--- Menú de Dibujo en Imágenes ---")
            print("1. Dibujar Rectángulo")
            print("2. Dibujar Línea")
            print("3. Dibujar Círculo")
            print("4. Mostrar Imagen")
            print("5. Guardar Imagen")
            print("6. Reiniciar Imagen")
            print("7. Salir")
            choice = input("Seleccione una opción (1-7): ")
            try:
                choice = int(choice)
                if choice == 1:
                    self.draw_rectangle()
                elif choice == 2:
                    self.draw_line()
                elif choice == 3:
                    self.draw_circle()
                elif choice == 4:
                    self.show_image()
                elif choice == 5:
                    self.save_image()
                elif choice == 6:
                    self.reset_image()
                    print("Imagen reiniciada a su estado original")
                elif choice == 7:
                    print("Saliendo del programa...")
                    break
                else:
                    print("Opción no válida. Intente de nuevo.")
            except ValueError:
                print("Entrada no válida. Por favor ingrese un número del 1 al 7.")

if __name__ == "__main__":
    # Entry point: ask for image path and start the menu
    image_path = input("Ingrese la ruta de la imagen: ")
    try:
        drawer = ImageDrawer(image_path)
        drawer.menu()
    except ValueError as e:
        print(e)
