/**
 * 
 */
package fraction;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

/**
 * Conducts arithmetic with fractions using the Fraction object and methods
 * created in the Fraction class.
 * @author Monica Rondon
 * @version November 21 2016
 */
public class FractionCalculator {
	
	/**
	 * Internal variable used to read user input.
	 */
	Scanner scanner = new Scanner(System.in);
	
	/**
	 * Holds current value of the calculator.
	 */
	private Fraction CurrentValue;
	
	/**
	 * Holds the fraction to be used in two factor operations.
	 */
	private Fraction one;
	
	/**
	 * Next command to be executed by the calculator.
	 */
	private String command = "";
	
	/**
	 * A list of valid commands.
	 */
	private ArrayList<String> ValidCommands = new ArrayList<String>(Arrays
			.asList("+", "-", "/", "*", "q", "a", "c", "i", "s" ));
	
	/**
	 * Prompts user and runs Fraction Calculator program.
	 * @param args not used
	 */
	public static void main(String[] args) {
		System.out.println("0");
		System.out.println("This is a Fraction Calculator.\n"
				+ "Enter a fraction, either as numerator/denominator"
				+ " or as a whole number.\n"
				+ "Then, chose what you would like to calcuate:\n"
				+ "\ta To take the absolute value of the number currently "
				+ "displayed\n"
				+ "\tc To clear (reset to zero) the calculator\n"
				+ "\ti To invert the number currently displayed\n"
				+ "\ts n To discard the number currently displayed and "
				+ "replace it with n\n"
				+ "\tq To quit the program\n"
				+ "\t+ n To add n to the number currently displayed\n"
				+ "\t- n To subtract n from the number currently displayed\n"
				+ "\t* n To multiply the number currently displayed by n\n"
				+ "\t/ n To divide the number currently displayed by n\n"
				+ "Enter your fractions and your command on seperate lines, "
				+ "as follows:\n"
				+ "Fraction\nCommand\nFraction");
		FractionCalculator calc = new FractionCalculator();
		calc.run();
	}

	/**
	 * Reads user input.
	 * If incorrect it will try again without crashing the program.
	 */
	public void ReadInput(){
		String input = scanner.next();
		System.out.println();
		if(input.length() == 1 && ValidCommands.contains(input)){
			command = input;
		} else {
			try{
				one = new Fraction(input);
				if(CurrentValue == null){
					CurrentValue = one;
					one = null;
				}
			} catch (Exception e) {
				InputError("That fraction was invalid");
			}
		}
	}
	
	/**
	 * Evaluates type of command user input.
	 * Either manipulating two fractions (commands +,-,/,*) or 
	 * changing/evaluating one fractions/quitting (commands q,i,a,c)
	 * @return true if calculator can execute a command, false otherwise
	 */
	public boolean CanExecute(){
		switch(command){
			// deliberate fall through.
			// all cases are "single factor"
			// such that a second value is not required
			case "q":
			case "i":
			case "a":
			case "c":
				return true;
			// deliberate fall through
			// all cases are two-factor
			// such that an additional value is required
			// to perform the operation
			case "+":
			case "-":
			case "*":
			case "/":
			case "s":
				if(one != null){
					return true;
				}
				return false;
			default:
				return false;
		}
	}
	
	/**
	 * Runs the calulator's main functionality in a loop until the user quits
	 */
	public void run(){
		ReadInput();
		if(CanExecute()){
			executeInput();
		}
		run();
	}
	
	/**
	 * Prints Input Error message
	 * @param message a string to be displayed to the user
	 */
	private void InputError(String message){
		System.out.println(message);
	}
	
	/**
	 * Executes the calculator command as passed to the method.
	 * Prints result and then prepares the calculator for the next execution.
	 * The calculator must be in a valid state before this is called.
	 */
	public void executeInput(){
		switch (command) {
	        case "+":
	        	CurrentValue = CurrentValue.add(one);
	            break;
	        case "-":  
	        	CurrentValue = CurrentValue.subtract(one);
	        	break;
	        case "/":  
	        	CurrentValue = CurrentValue.divide(one);
	        	break;
	        case "*":  
	        	CurrentValue = CurrentValue.multiply(one);
	        	break;
	        case "q":  
	        	System.out.println("Goodbye!");
	        	System.exit(0);
	        	break;
	        case "a":
	        	CurrentValue = CurrentValue.abs();
	        	break;
	        case "c":
	        	CurrentValue = null;
	        	one = null;
	        	command = "";
	        	System.out.println("0");
	        	return;
	        case "i":
	        	CurrentValue = CurrentValue.inverse();
	            break;
	        case "s":
	            CurrentValue = one;
	        	break;
	        default: 
	        	break;
		}
		command = "";
		one = null;
		System.out.println(CurrentValue.toString());
		System.out.println("\nEnter a Fraction or a Command:");
	    return;
	}
}
