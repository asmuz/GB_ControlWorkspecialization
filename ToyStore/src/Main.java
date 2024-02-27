import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        ToyStore toyStore = new ToyStore();
        toyStore.addToy(new Toy(1, "Кукла", 5, 20));
        toyStore.addToy(new Toy(2, "Машинка", 5, 30));
        toyStore.addToy(new Toy(3, "Медвежонок", 5, 50));
        toyStore.addToy(new Toy(4, "Кубики", 5, 40));
        toyStore.addToy(new Toy(5, "Мяч", 5, 25));
        toyStore.addToy(new Toy(6, "Конструктор", 5, 35));

        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("Игрушки в розыгрыше:");
            for (Toy toy : toyStore.getToys()) {
                System.out.println(toy.getName() + " (" + toy.getQuantity() + " шт)");
            }
            System.out.println("\nМеню:");
            System.out.println("1. Разыграть игрушку");
            System.out.println("0. Выйти");
            System.out.print("\nВыберите действие: ");
            int choice = scanner.nextInt();
            scanner.nextLine();

            if (choice == 1) {
                Toy selectedToy = toyStore.selectToy();
                clearConsole();
                if (selectedToy != null) {
                    System.out.println("\nВаш приз: " + selectedToy.getName() + "!");
                    toyStore.saveToyToFile(selectedToy);
                    System.out.print("\nНажмите ENTER для продолжения...");
                    scanner.nextLine();
                    clearConsole();
                } else {
                    System.out.println("Извините, все игрушки разыграны...");
                }
            } else if (choice == 0) {
                System.out.println("Всего доброго!");
                break;
            } else {
                System.out.println("Неверный выбор. Пожалуйста, введите число 1 или 0.");
            }
        }

        scanner.close();
    }
    public static void clearConsole() {
        for (int i = 0; i < 20; i++) {
            System.out.println();
        }
    }
}
