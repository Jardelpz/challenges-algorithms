import java.util.Scanner;

public class tabuada {

	public static void main(String[] args) {
		Scanner j = new Scanner(System.in);

		System.out.println("Número: ");
		int n = j.nextInt();

		for (int i = 0; i < 11; i++) {
			System.out.println(n + "*" + i + " = " + n * i);
		}

	}

}