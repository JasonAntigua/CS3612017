/**
 * @author Jason Antigua 
 * 		   Cooperated with Niaz 
 * 
 */
public class ScannerDemo {

	private static String file1 = "prog2.jay";
	private static int counter = 1;

	public static void main(String args[]) {

		TokenStream ts = new TokenStream(file1);

		System.out.println(file1);
		
		Token t;
		
		while (!ts.isEndofFile()) {
			t = ts.nextToken();
			System.out.println("Token " + counter + " - Type: " + t.getType() + " - Value: " + t.getValue() );
			t.toString();
			counter = counter + 1;
		}
	}
}
