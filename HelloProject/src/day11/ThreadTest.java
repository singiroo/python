package day11;

public class ThreadTest {
	public static void main(String[] args) {
	
		new Thread() {
			@Override
			public void run() {
				try {
					Thread.sleep(5000);
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
				System.out.println("hello");
			}
		}.start();
		
	}
}
