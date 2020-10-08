package day10;

import java.util.ArrayList;

public class ArrayListTest {
	
	public static void main(String[] args) {
		ArrayList<String> arr = new ArrayList<>();
		
		arr.add("»ç°ú");
		arr.add("±Ö");
		arr.add(0, "¸ÇÀ§");
		
		for(int i=0; i<arr.size();i++) {
			System.out.println(arr.get(i));
		}
		
	}
}
