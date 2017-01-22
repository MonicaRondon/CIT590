/**
 * 
 */
package cipher;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

/**
 *Caeser Cipher program encodes text by shifting position of letter in alphabet
 * @author Monica Rondon
 * @version November 26, 2016
 */
public class Caesar {

	/**
	 * Imported word txt file to compare deciphered txt to.
	 */
	public ArrayList<String> words;
	
	private int alphabetLength = 26;
	
	private int charShift(int min, int max, int charCode, int shift){
		if(charCode >= min && charCode <= max){
			charCode += shift;
			if(charCode > max){
				charCode -= alphabetLength;
			}
		}
		return charCode;
	}
	
	/**
	 * Shifts character position to encipher single character.
	 * Calls charShift, which sets shift for English language characters.
	 * @param shift number of positions to shift
	 * @param character to be shifted
	 * @return 'Shifted character'
	 * @throws IOException 
	 */
	public char cipheredCharacter(int shift, char character){
		shift = shift % 26;
		int charCode = (int) character;
		charCode = charShift(65, 90, charCode, shift);
		charCode = charShift(97, 122, charCode, shift);
		return (char)charCode;
	}
	
	/**
	 * Enciphers message, using shift. 
	 * Shift allowed to be any integer value.
	 * @param shift number of positions to shift
	 * @param plainText text to be shifted
	 * @return "Enciphered text"
	 */
	public String encipher(int shift, String plainText){
		char[] chars = plainText.toCharArray();
		for(int i = 0; i < chars.length; i++){
			chars[i] = cipheredCharacter(shift, chars[i]);
		}
		return String.valueOf(chars);
	}
	
	
	/**
	 * Creates confidence rating for each possible deciphered text.
	 * Used to ascertain the encryption most likely used on CryptedText.
	 */
	public double testConfidence(String text){
		int badWords = 0;
		//http://stackoverflow.com/questions/1805518/replacing-all-non-
		//alphanumeric-characters-with-empty-strings
		text = text.replaceAll("/[A-Za-z ]/", "");
		if(text.length() == 0){
			return 0.0;
		}
		//http://stackoverflow.com/questions/7899525/how-to-split-a-string-by-
		//space
		String[] textWords = text.split("\\s+");
		for(String word : textWords){
			if(!words.contains(word.toLowerCase())){
				badWords++;
			} 
		}
		return 1.0 - ((double)badWords / (double)textWords.length);
	}
	
	/**
	 * Deciphers message enciphered using a Caesar Cipher.
	 * @param cipheredText text shifted 
	 * @return "Deciphered text" 
	 */
	public String decipher(String cipheredText) throws IOException{
		String bestGuess = "";
		double highestConfidence = 0.0;
		loadWords();
		for(int i = 0; i < 26; i++){
			String decipheredText = encipher(i, cipheredText);
			double confidence = testConfidence(decipheredText);
			if(confidence > highestConfidence){
				highestConfidence = confidence;
				bestGuess = decipheredText;
			}
		}
		return bestGuess;
		
	}
	
	/**
	 * Loads word list to compare deciphered text to.
	 * @throws IOException
	 */
	public void loadWords() throws IOException{
		words = new ArrayList<String>();
		//load file
		Scanner wordFile = new Scanner(new File("wordsEn.txt"));
		//loop file
		while (wordFile.hasNextLine()) {
			String word = wordFile.nextLine().trim();
			if(word.length() > 0){
				words.add(word);				
			}
		}
		wordFile.close();
	}


}
