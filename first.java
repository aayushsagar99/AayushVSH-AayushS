import java.util.*;
import java.util.concurrent.*;
import java.util.stream.*;

public class ComplexProcessor<T extends Number> {

    private final List<T> data;
    private final ExecutorService executor;

    public ComplexProcessor(List<T> data) {
        this.data = Collections.unmodifiableList(data);
        this.executor = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
    }

    public CompletableFuture<Double> processDataAsync() {
        return CompletableFuture.supplyAsync(() -> {
            return data.parallelStream()
                .mapToDouble(Number::doubleValue)
                .filter(val -> val > 0)
                .map(val -> Math.pow(val, 2))
                .average()
                .orElse(0.0);
        }, executor);
    }

    public Map<String, List<T>> categorizeData(double threshold) {
        return data.stream().collect(Collectors.groupingBy(val -> 
            val.doubleValue() > threshold ? "HIGH" : "LOW"
        ));
    }

    public void shutdown() {
        executor.shutdown();
        try {
            if (!executor.awaitTermination(5, TimeUnit.SECONDS)) {
                executor.shutdownNow();
            }
        } catch (InterruptedException e) {
            executor.shutdownNow();
            Thread.currentThread().interrupt();
        }
    }

    public static void main(String[] args) {
        List<Integer> numbers = IntStream.range(1, 1000)
            .boxed()
            .collect(Collectors.toList());

        ComplexProcessor<Integer> processor = new ComplexProcessor<>(numbers);

        processor.processDataAsync()
            .thenAccept(result -> System.out.printf("Processed Average: %.2f%n", result))
            .join();

        Map<String, List<Integer>> categories = processor.categorizeData(500.0);
        System.out.println("High count: " + categories.get("HIGH").size());

        processor.shutdown();
    }
}
