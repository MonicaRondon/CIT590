/**
 * 
 */
package fraction;
import static org.junit.Assert.*;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

import org.junit.Test;

/**
 * @author Monica Rondon
 * @version November 21 2016
 *Tests constructors and methods of Fraction class.
 */
public class FractionTest {

	Fraction f; 
	
	@Test
	public final void testFractionIntInt() {
		f = new Fraction(1,2);
		assertEquals("1/2", f.toString());
		f = new Fraction(0,5);
		assertEquals("0/1", f.toString());
	}

	@Test(expected=ArithmeticException.class)
	public final void testFractionIntIntZeroDenominatorThrowsException() {
		f = new Fraction(1, 0);
	}

	
	@Test
	public final void testFractionInt() {
		f = new Fraction(5);
		assertEquals("5/1", f.toString());
		f = new Fraction(0);
		assertEquals("0/1", f.toString());
	}

	@Test
	public final void testFractionString() {
		f = new Fraction("5"); 
		assertEquals("5/1", f.toString());
		f = new Fraction("4/-6");
		assertEquals("-2/3", f.toString());
		f = new Fraction("8/ -12");
		assertEquals("-2/3", f.toString());
		f = new Fraction("-3");
		assertEquals("-3/1", f.toString());
	}	
	
	@Test(expected=NumberFormatException.class)
	public final void testFractionStringMalformedStringThrowsException() {
		f = new Fraction("this doesn't work");
	}
	
	
	@Test
	public final void testAdd() {
		f = new Fraction(2);
		Fraction f2 = new Fraction(2, 4);
		assertEquals("5/2", f.add(f2).toString());
		f = new Fraction(2, -4);
		f2 = new Fraction(1, 2);
		assertEquals("0/1", f.add(f2).toString());
	}

	@Test
	public final void testSubtract() {
		f = new Fraction(2);
		Fraction f2 = new Fraction(2, 4);
		assertEquals("3/2", f.subtract(f2).toString());
		f = new Fraction(2, -4);
		f2 = new Fraction(1, 2);
		assertEquals("-1/1", f.subtract(f2).toString());
	}

	@Test
	public final void testMultiply() {
		f = new Fraction(2);
		Fraction f2 = new Fraction(2, 4);
		assertEquals("1/1", f.multiply(f2).toString());
		f = new Fraction(2, -4);
		f2 = new Fraction(1, 2);
		assertEquals("-1/4", f.multiply(f2).toString());
	}

	@Test
	public final void testDivide() {
		f = new Fraction(2);
		Fraction f2 = new Fraction(2, 4);
		assertEquals("4/1", f.divide(f2).toString());
		f = new Fraction(2, -4);
		f2 = new Fraction(1, 2);
		assertEquals("-1/1", f.divide(f2).toString());
	}

	@Test
	public final void testAbs() {
		f = new Fraction(-2, 4);
		assertEquals("1/2", f.abs().toString());
	}

	@Test
	public final void testNegate() {
		f = new Fraction(-2, 4);
		assertEquals("1/2", f.negate().toString());
		f = new Fraction(2, 4);
		assertEquals("-1/2", f.negate().toString());
		f = new Fraction(0, 1);
		assertEquals("0/1", f.negate().toString());
	}

	@Test
	public final void testInverse() {
		f = new Fraction(-2, 4);
		assertEquals("-2/1", f.inverse().toString());
		f = new Fraction(4, 2);
		assertEquals("1/2", f.inverse().toString());

	}
	
	@Test(expected=ArithmeticException.class)
	public final void testInverseZeroThrowsException() {
		f = new Fraction(0, 2);
		f.inverse();
	}

	@Test
	public final void testEqualsObject() {
		f = new Fraction(1);
		assertFalse(f.equals(new Object()));
		assertTrue(f.equals(new Fraction(2, 2)));
		f = new Fraction(2);
		assertFalse(f.equals(new Fraction(1, 2)));
		f = new Fraction(-1, 2);
		assertTrue(f.equals(new Fraction(1, -2)));
	}

	@Test
	public final void testCompareTo(){
		f = new Fraction(2);
		Fraction f2 = new Fraction(2, 4);
		assertEquals(f.compareTo(f2), 1);
		assertEquals(f.compareTo(1), 1);
		assertEquals(f.compareTo(0), 1);
		assertEquals(f.compareTo(-1), 1);
		f = new Fraction(2);
		f2 = new Fraction(4, 2);
		assertEquals(f.compareTo(f2), 0);
		assertEquals(f.compareTo(2), 0);
		f = new Fraction(1, 3);
		f2 = new Fraction(2, 4);
		assertEquals(f.compareTo(f2), -1);
		assertEquals(f.compareTo(1), -1);
	}
	
	@Test(expected=ClassCastException.class)
	public final void testCompareTo_exception() {
		f = new Fraction(1, 3);
		f.compareTo("This won't work it is not an int or a fraction");
	}

	@Test
	public final void testToString() {
		f = new Fraction(1,2);
		assertEquals("1/2", f.toString());
		f = new Fraction(2,4);
		assertEquals("1/2", f.toString());
		f = new Fraction(2,2);
		assertEquals("1/1", f.toString());
		f = new Fraction(2);
		assertEquals("2/1", f.toString());
	}
	
	@Test
	public final void testGCD() {
		//Sourcecode: http://stackoverflow.com/questions/11483647/
		//how-to-access-private-methods-and-private-data-members-via-reflection
		f = new Fraction(1); // this part is irrelevant 
		Method m;
		try {
			m = Fraction.class.getDeclaredMethod("GCD", int.class, int.class);
	        m.setAccessible(true);
	        //Sourcecode: http://stackoverflow.com/questions/13336057/
	        //java-reflection-object-is-not-an-instance-of-declaring-class
	        int result = (int)m.invoke(f, 4, 8);
	        assertEquals(result, 4);
	        assertEquals((int)m.invoke(f, 12, 30), 6);
	        assertEquals((int)m.invoke(f, 12, -30), 6);
	        assertEquals((int)m.invoke(f, -12, -30), 6);
	        assertEquals((int)m.invoke(f, -12, 30), 6);
	        assertEquals((int)m.invoke(f, 0, 30), 1);
	        assertEquals((int)m.invoke(f, 12, 0), 1);
	        
		} catch (NoSuchMethodException e) {
			e.printStackTrace();
		} catch (SecurityException e) {
			e.printStackTrace();
		} catch (IllegalAccessException e) {
			e.printStackTrace();
		} catch (IllegalArgumentException e) {
			e.printStackTrace();
		} catch (InvocationTargetException e) {
			e.printStackTrace();
		}
	}
}
