package Test;

public class CallbyRef {
	
	//a => value
	public static void add(int a) {
		a++;
	}
	
	public static void addRef(int[] a) {
		a[0]++;
	}
	
	
	public static void main(String[] args) {
		int a =1;
		int[] b = {3};
		System.out.println("a:"+a);
		System.out.println("b:"+b[0]);
		
		add(a);
		addRef(b);
			
		System.out.println("a:"+a);
		System.out.println("b:"+b[0]);
		
		
	}
	
	
	
	
	
}
