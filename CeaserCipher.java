import java.util.Scanner;

public class CeaserCipher {
	
	static String encrypt(String plaintext, int key) {
		StringBuilder ciphertext = new StringBuilder();
		
		for(char ch: plaintext.toCharArray()) {
			
			char cipherChar = (char)((((ch - 'A') + key) % 26) + 'A');
			ciphertext.append(cipherChar);
		}
		
		return ciphertext.toString();
		
	}
	
	static String decrypt(String ciphertext, int key) {
		return encrypt(ciphertext, 26 - key);
	}
	
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		
		System.out.println("Enter Plaintext");
		String plaintext = sc.nextLine();
		plaintext = plaintext.toUpperCase();
	
		
		System.out.println("Enter Key");
		int key = sc.nextInt();
		
		sc.close();

		System.out.println("Your Plaintext is " + plaintext + " with key " + key);
				
		String ciphertext = encrypt(plaintext, key);
		System.out.println("Cipher Text is\t" + ciphertext);
		
		String deciphertext = decrypt(ciphertext, key);
		System.out.println("Decipher Text is\t" + deciphertext);
		
		
	}
}