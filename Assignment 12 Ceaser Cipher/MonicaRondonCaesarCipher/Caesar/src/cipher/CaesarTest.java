package cipher;

import static org.junit.Assert.*;

import java.io.IOException;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;

public class CaesarTest {
	
	Caesar c;
	@BeforeClass
	public static void setUpBeforeClass() throws Exception {
	}

	@Before
	public void setUp() throws Exception {
		//runs before every test
		c = new Caesar();
	}

	@Test
	public void testcipheredCharacter(){
		assertEquals('A', c.cipheredCharacter(0, 'A'));
		assertEquals('C', c.cipheredCharacter(2, 'A'));
		assertEquals('Z', c.cipheredCharacter(25, 'A'));
		assertEquals('c', c.cipheredCharacter(2, 'a'));
		assertEquals('z', c.cipheredCharacter(26, 'z'));
		assertEquals('a', c.cipheredCharacter(27, 'z'));	
	}
	@Test
	public void testEncipher() {
		assertEquals("Vguv", c.encipher(2, "Test"));
		assertEquals("Test", c.encipher(0, "Test"));
		assertEquals("Sdrs", c.encipher(25, "Test"));
		assertEquals("Vjku ku c vguv.", c.encipher(2, "This is a test."));
	}

	@Test
	public void testDecipher() throws IOException {
		assertEquals("Test", c.decipher("Vguv"));
		assertEquals("Test", c.decipher("Test"));
		assertEquals("Test", c.decipher("Sdrs"));
		assertEquals("This is a test.", c.decipher("Vjku ku c vguv."));
		assertEquals("This is a test.", c.decipher("Vjku ku c vguv."));
		assertEquals("If you can read this, you probably have completed"
				+ " the Caesar Cipher assignment.", c.decipher("Mj csy "
						+ "ger vieh xlmw, csy tvsfefpc lezi gsqtpixih xli "
						+ "Geiwev Gmtliv ewwmkrqirx."));
	}
	
	@Test
	public void testloadWords() throws IOException {
		c.loadWords();
		assertEquals(109582, c.words.size());
		assertTrue(c.words.contains("abandon"));
		assertFalse(c.words.contains("selfie-kakakakaak")); // do not add to wordlist or this will fail
	}
	

}
