/**
 * 
 */
package fraction;

/**
 * Creates Fraction object and methods for calculation. 
 * @author Monica Rondon
 * @version November 21 2016
 */
public class Fraction implements Comparable{
	
	/**
	 * the top of the fraction
	 */
	private int numerator;
	/**
	 * the bottom of the fraction
	 */
	private int denominator;

	/**
	 * Establishes rules for all Fraction objects, called by all constructors.
	 * Does not have a unit test because it is tested by every other 
	 * constructor calling it.
	 * @param numerator the top of the fraction
	 * @param denominator the bottom of the fraction.
	 * @exception ArithmeticException division by zero not allowed
	 */
	private void initialize(int numerator, int denominator) throws ArithmeticException {
		if(denominator == 0){
			throw new ArithmeticException("Can't divide by zero");
		}
		if(numerator == 0){
			this.numerator = 0;
			this.denominator = 1;
			return;
		}
		int GCD = this.GCD(numerator, denominator);
		this.numerator = numerator / GCD;
		this.denominator = denominator / GCD;
		if(this.denominator < 0){
			this.numerator = this.numerator * -1;
			this.denominator = this.denominator * -1;
		}
	}
	
	/**
	 * 
	 * Constructs Fraction object composed of a numerator and denominator. 
	 * @param numerator the top of the fraction
	 * @param denominator the bottom of the fraction
	 * @exception ArithmeticException if there is a divide by zero error
	 */
	public Fraction(int numerator, int denominator) throws ArithmeticException {
		// The value of calling the shared intialize method is that it allows
		// all complex and error checking logic to be written only once.
		initialize(numerator, denominator);
	}
	
	/**
	 * Constructs Fraction object composed of a whole number.
	 * Parameter is the numerator and 1 is the implicit denominator.
	 * @param wholeNumber an integer to be converted into a fraction
	 */
	public Fraction(int wholeNumber) {
		// The value of calling the shared intialize method is that it allows
		// all complex and error checking logic to be written only once.
		initialize(wholeNumber, 1);
	}
	
	/**
	 * Constructs Fraction object composed of a String.
	 * @param fraction in the format "1/2", "3/4", and so on.
	 * @exception ArithmeticException if a divide by zero happens
	 * @exception NumberFormatException if the format is not an acceptable fraction
	 */
	public Fraction(String fraction) throws ArithmeticException, NumberFormatException {
		// The value of calling the shared intialize method is that it allows
		// all complex and error checking logic to be written only once.
		String[] parts = fraction.split("/");
		if(parts.length > 2){
			throw new NumberFormatException(fraction + " "
					+ "is not a valid Fraction.");
		}
		int n, d;
		n = Integer.parseInt(parts[0].trim());
		if(parts.length == 1){
			d = 1;
		} else {
			d = Integer.parseInt(parts[1].trim());
		}
		initialize(n, d);
	}
	
	/**
	 * Returns a new Fraction that is the sum of this and f.
	 *  a/b + c/d
	 * @param f another fraction to be added to this
	 * @return a new Fraction 
	 */
	public Fraction add(Fraction f){
		int a, b, c, d;
		a = numerator;
		b = denominator;
		c = f.numerator;
		d = f.denominator;
		return new Fraction((a * d + b * c), b * d);
	}
	
	/**
	 * Returns a new Fraction that is the difference of this minus f.
	 * a/b - c/d
	 * @param f another fraction to be subtracted from this
	 * @return a new Fraction
	 */
	public Fraction subtract(Fraction f){
		int a, b, c, d;
		a = numerator;
		b = denominator;
		c = f.numerator;
		d = f.denominator;
		return new Fraction((a * d - b * c), b * d);
	}
	
	/**
	 * Returns a new Fraction that is the product of this and f.
	 * a/b * c/d
	 * @param f another fraction to multiply this by
	 * @return a new Fraction
	 */
	public Fraction multiply(Fraction f){
		int a, b, c, d;
		a = numerator;
		b = denominator;
		c = f.numerator;
		d = f.denominator;
		return new Fraction(a * c, b * d);
	}
	
	/**
	 * Returns a new Fraction that is the quotient of dividing this by f.
	 * a/b / c/d
	 * @param f another fraction to divide this by
	 * @return a new Fraction
	 */
	public Fraction divide(Fraction f){
		int a, b, c, d;
		a = numerator;
		b = denominator;
		c = f.numerator;
		d = f.denominator;
		return new Fraction(a * d, b * c);
	}

	/**
	 * Returns a new Fraction that is the absolute value of this fraction.
	 * @return a new Fraction 
	 */
	public Fraction abs(){
		return new Fraction(Math.abs(numerator), Math.abs(denominator));
	}
	
	/**
	 * Returns a new Fraction that has the same numeric value of this fraction, but the opposite sign. 
	 * @return a new Fraction
	 */
	public Fraction negate(){
		return new Fraction(numerator * -1, denominator);
	}
	
	/**
	 * Sets the numerator to the denominator of this Fraction and vice versa.
	 * @return a new Fraction 
	 */
	public Fraction inverse(){
		return new Fraction(denominator, numerator);
	}
	
	/**
	 * Returns true if o is a Fraction equal to this, and false otherwise.
	 * @param o an object to test against this fraction
	 * @return true if equal, false if not.
	 */
	@Override
	public boolean equals(Object o){
		if (!(o instanceof Fraction)){
			return false;
		}
		Fraction f = (Fraction)o;
		if(numerator == f.numerator && denominator == f.denominator){
			return true;
		}
		return false;
	}
	
	/**
	 * Compares this Fraction to an Integer or another fraction.
	 * Returns:
	 * 	-1 	if this is less than o
	 * 	 0	if this is equal to o
	 * 	 1	if this is greater than o.
	 * @param o an object to compare this fraction to
	 * @return -1, 0, or 1
	 * @exception ClassCastException if o is not a fraction or Integer
	 */
	@Override
	public int compareTo(Object o) {
		Fraction comp;
		if(o instanceof Fraction){
			comp = (Fraction)o;
		}else if(o instanceof Integer){
			comp = new Fraction((int)o);
		} else {
			throw new ClassCastException("You must compare to another Fraction"
					+ " or an Integer");
		}
		Fraction result = subtract(comp);
		if(result.numerator < 0){
			return -1;
		} else if(result.numerator > 0){
			return 1;
		}
		return 0;
	}
	
	/**
	 * Returns a String of the form n/d.
	 * n is the numerator and d is the denominator.
	 * @return numerator/denominator
	 */
	@Override
	public String toString(){
		return numerator + "/" + denominator;
	}
	
	/**
	 * Calculates Greatest Common Divisor (GCD) of two numbers. 
	 * @param one the first number to check
	 * @param two the second number to check
	 * @return GCD of two numbers
	 */
	private int GCD(int one, int two){
		one = Math.abs(one);
		two = Math.abs(two);
		if(one == 0 || two == 0){
			return 1;
		}
		if(one == two){
			return one;
		}
		int next;
		if (one > two){
			next = one % two;
			if(next == 0){
				return two;
			}
			one = next;
		}
		else {
			next = two % one;
			if(next == 0){
				return one;
			}
			two = next;
		}
		return GCD(one, two);
	}
}
