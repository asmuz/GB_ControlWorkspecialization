import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class ToyStore {
    private List<Toy> toys;

    public ToyStore() {
        toys = new ArrayList<>();
    }

    public void addToy(Toy toy) {
        toys.add(toy);
    }

    public void updateToyWeight(int id, double weight) {
        for (Toy toy : toys) {
            if (toy.getId() == id) {
                toy.setWeight(weight);
                return;
            }
        }
        System.out.println("Игрушка с id " + id + " не найдена.");
    }

    public Toy selectToy() {
        double totalWeight = toys.stream().mapToDouble(Toy::getWeight).sum();
        double randomNumber = Math.random() * totalWeight;
        double cumulativeWeight = 0;
        for (Toy toy : toys) {
            cumulativeWeight += toy.getWeight();
            if (randomNumber <= cumulativeWeight) {
                Toy selectedToy = new Toy(toy.getId(), toy.getName(), 1, toy.getWeight());
                toy.decreaseQuantity();
                if (toy.getQuantity() == 0) {
                    toys.remove(toy);
                }
                return selectedToy;
            }
        }
        return null;
    }

    public void saveToyToFile(Toy toy) {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter("winners.txt", true))) {
            writer.write("Игрушка: " + toy.getName() + ", ID: " + toy.getId() + "\n");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public List<Toy> getToys() {
        return toys;
    }
}
