
import java.util.Scanner;

public class primo {

	public static void main(String[] args) {
		Scanner j = new Scanner(System.in);

		System.out.println("Número: ");
		int n = j.nextInt();
		boolean n_primo = false;
		for (int i = 2; i < n; i++) {
			if((n% i == 0)) {
				n_primo=true;
				break;
			}
		}
		
		if(n_primo) {
			System.out.println("Não é primo");
		}else {
			if(n>=0 & (n<2)) {
				System.out.println("Não é primo");
			}else {
				System.out.println("Primo");
			}
						
		}

	}

}