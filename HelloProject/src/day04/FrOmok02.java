package day04;

import java.awt.BorderLayout;
import java.awt.EventQueue;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.ImageIcon;

/**
 * 오목 게임을 만드는 클래스
 * @author PC-25
 *
 */
public class FrOmok02 extends JFrame {

	private JPanel contentPane;										//GUI 윈도우 창
	private JLabel[] arr2D = new JLabel[10];						//JLabel을 10개 저장할 수 있는 배열
	private JLabel[][] arr2 = new JLabel[10][10];					//JLabel을 10개 저장할 수 있는 배열을 10개 저장할 수 있는 2차원 배열? --> 게임의 출력판
	private int[][]	int2d = new int[10][10];						//int 값을 10x10개 저장할 수 있는 2차원 배열 --> 게임의 로직판
	private ImageIcon iie = new ImageIcon(FrOmok02.class.getResource("/day04/0.jpg"));			//바둑판 이미지를 저장한 ImageIcon 객체
	private ImageIcon iiw = new ImageIcon(FrOmok02.class.getResource("/day04/1.jpg"));			//백색돌 이미지를 저장한 ImageIcon 객체
	private ImageIcon iib = new ImageIcon(FrOmok02.class.getResource("/day04/2.jpg"));			//흑색돌 이미지를 저장한 ImageIcon 객체
	private boolean turn = false;									//플레이어의 턴을 알려주는 플래그
	private boolean flagIng = true;									//게임이 진행 중임을 알려주는 플래그
	private String winner = "";										//승자가 누구인지를 저장하는 String 객체

	/**
	 * Launch the application.
	 */
	// 스레드 동작.
	// 스레드 생성 및 호출 제 3방법으로 Runnable인터페이스의 run()메서드를 구현하여 사용
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					FrOmok02 frame = new FrOmok02(); // 생성자 호출 --> 객체 생성
					frame.setVisible(true);          // 오목 게임 윈도우를 가시화
				} catch (Exception e) {
					e.printStackTrace();
				}
				
			}
			
		}); // 익명 클래스? 의 구현
	}
	
	
	/**
	 * 게임의 로직을 담당하는 로직판을 출력하는 메서드
	 * 
	 */
	public void showInt2d() {
		for(int i=0;i<int2d.length;i++) {
			for(int j=0;j<int2d[i].length;j++) {
				System.out.print("\t"+int2d[i][j]);
			}
			System.out.println();
		}
	}
	
	/**
	 * 로직판의 정보를 바탕으로 게임의 출력판의 아이콘 배치를 하는 메서드
	 */
	public void myRender() {
		for(int i=0;i<int2d.length;i++) {
			for(int j=0;j<int2d[i].length;j++) {
				int data = int2d[i][j];
				if(data == 0) {
					arr2[i][j].setIcon(iie);
				}else if(data == 1) {
					arr2[i][j].setIcon(iiw);
				}else {
					arr2[i][j].setIcon(iib);
				}
			}
		}
	}
	
	
	/**
	 * Create the frame.
	 * 생성자
	 */
	
	public FrOmok02() {
		//windowbuilder를 이요하여 만든 창의 설정들
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 812, 691);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
	
		// 
		for(int j=0;j<arr2.length;j++) {
			for(int i=0; i<arr2[j].length; i++) { 
				JLabel lbl = new JLabel("New label"); // JLavel 객체 생성
				lbl.setIcon(iie);	// 기본 아이콘인 바둑판 아이콘으로 설정
				lbl.setText(j+","+i);	// 라벨에 좌표정보를 기록
				lbl.setBounds(0+(75*i), 0+(75*j), 75, 75);	// 라벨의 위치를 설정
				contentPane.add(lbl);   // 바탕이 되는 gui창에 라벨 요소를 추가
				arr2D[i] = lbl; // 라벨을 일렬로 저장하여 가로 줄 하나를 만듬
				arr2[j][i] = lbl; // 라벨을 2차원 배열로 저장하여 게임판을 만듬. 게임의 출력판을 2차원 배열로 나타냄
				lbl.addMouseListener(new MouseAdapter() { // 마우스 동작에 따른 이벤트를 생성
					@Override
					public void mouseClicked(MouseEvent e) {
						myclick(e); // 로직판을 생성
					}
				});
			}
		}
			
		showInt2d(); // 로직판을 출력하고
		myRender(); // 로직판을 기반으로 게임의 출력판을 출력
		
	}
	
	/**
	 * 게임의 전반적인 로직을 처리하는 메서드
	 * @param e
	 */
	public void myclick(MouseEvent e) {
		
//		if(!flagIng)) {
//			return;
//		}
		
		JLabel temp = (JLabel)e.getComponent(); // 이벤트가 일어나는 발생지 즉, 클릭한 요소를 가져오는 메서드
		System.out.println(temp.getText()); // 라벨에 기록된 좌표정보를 출력
		String locator = temp.getText(); // 라벨에 기록된 2차원 배열에서의 좌표정보를 얻어옴
		String[] location = locator.split(","); // 좌표를 숫자 형태로 바꾸기 위해 가공중
		int x = Integer.parseInt(location[0]); // i 좌표 (큰방 번호)를 저장
		int y = Integer.parseInt(location[1]); // j 좌표 (작은 방 번호)를 저장
		
		//중복된 위치에 두는 것을 방지하기 위해 바둑판이 아닌 곳에 두면 메세지와 함께 메서드 종료
		if(temp.getIcon() != iie) {
			System.out.println("중복된 위치입니다!!");
			return;
		}
		
		// 백색 돌 (1)
		int cnt_stone = 1; // 현재 턴의 주인 돌의 종류 => 0 : 바둑판 , 1 : 백색돌, 2 : 흑색돌
		
		
		// 턴에 따라 클릭한 위치를 흰돌 / 흑색돌로 바꿈.
		if(turn) {
			int2d[x][y] = 1;
			cnt_stone = 1;
		}else{
			int2d[x][y] = 2;
			cnt_stone = 2;
		}
		
		myRender(); // 로직판의 수치 값의 변경을 바탕으로 출력판에 결과를 출력함
		
		int up_cnt = getUp(x, y, cnt_stone); // 놓은 돌을 기점으로 위에 존재하는 같은 돌의 갯수
		int dw_cnt = getDown(x, y, cnt_stone); // 놓은 돌을 기점으로 아래에 존재하는 같은 돌의 갯수
		int left_cnt = getLeft(x, y, cnt_stone); // 놓은 돌을 기점으로 왼쪽에 존재하는 같은 돌의 갯수
		int right_cnt = getRight(x, y, cnt_stone); // 놓은 돌을 기점으로 오른쪽에 존재하는 같은 돌의 갯수
		
		int uple_cnt = getUpLe(x, y, cnt_stone); // 놓은 돌을 기점으로 대각선 왼쪽 위에 존재하는 같은 돌의 갯수
		int upRi_cnt = getUpRi(x, y, cnt_stone); // 놓은 돌을 기점으로 대각선 오른쪽 위에 존재하는 같은 돌의 갯수
		int dwle_cnt = getdwLe(x, y, cnt_stone); // 놓은 돌을 기점으로 대각선 왼쪽 아래에 존재하는 같은 돌의 갯수
		int dwRi_cnt = getdwRi(x, y, cnt_stone); // 놓은 돌을 기점으로 대각선 오른쪽 아래에 존재하는 같은 돌의 갯수
		
		
		int[] cnt5p = new int[4]; // 4방의 같은 색의 돌 갯수를 저장하기 위한 배열
		
		cnt5p[0] = up_cnt + dw_cnt + 1; // 세로방향의 돌의 갯수
		cnt5p[1] = left_cnt + right_cnt + 1; // 가로방향의 돌의 갯수
		cnt5p[2] = uple_cnt + dwRi_cnt + 1; //  좌측 대각선 방향의 돌의 갯수
		cnt5p[3] = upRi_cnt + dwle_cnt + 1; // 우측 대각선 방향의 돌의 갯수
		
		
		// 각 방향의 돌의 갯수가 정확히 5일 때 턴의 정보를 바탕으로 승패를 판정하고 승리 메세지를 출력한다
		// 게임 진행 중임을 알려주는 플래그를 게임 종료로 전환한다.
		for(int cnt : cnt5p) {
			if(cnt == 5) {
			  winner = 	turn == true ? "백돌" : "흑돌";
			  JOptionPane.showMessageDialog(null, winner+"이 이겼습니다.");	
			  flagIng = !flagIng;
//			  System.exit(0);
			}
		}
		
		
		
		System.out.println("up : "+up_cnt);
		System.out.println("down : "+dw_cnt);
		System.out.println("left : "+left_cnt);
		System.out.println("right : "+right_cnt);
		System.out.println("upleft : "+uple_cnt);
		System.out.println("upright : "+upRi_cnt);
		System.out.println("downleft : "+dwle_cnt);
		System.out.println("downright : "+dwRi_cnt);
		
		
		// 모든 처리가 완료 되었을 때 턴의 교대
		// kisamano turn da!
		turn = !turn;
	}
	
	
	
	
	
	
	/**
	 * 위쪽 방향으로 같은 돌의 갯수를 카운팅 하는 메서드
	 * @param x		플레이어가 놓은 돌의 i좌표
	 * @param y		플레이어가 놓은 돌의 j좌표
	 * @param cnt_stone		플레이어가 놓은 돌의 종류
	 * @return				플레이어가 놓은 돌의 종류와 같은 돌의 갯수
	 */
	public int getUp(int x, int y, int cnt_stone) {
		int cnt = 0;
		//숙제
		try {
			while(true) {
				if(int2d[--x][y] == cnt_stone) {  // x가 음수 값이 되면 안되기 때문에 try-catch 구문으로 exception 처리
					cnt++;
				}else {
					break;
				}
			}
		}catch(IndexOutOfBoundsException e) {
			System.out.println("line out");
		}
		
		return cnt;			
	}
	/**
	 * 아래쪽 방향으로 같은 돌의 갯수를 카운팅 하는 메서드
	 * @param x		플레이어가 놓은 돌의 i좌표
	 * @param y		플레이어가 놓은 돌의 j좌표
	 * @param cnt_stone		플레이어가 놓은 돌의 종류
	 * @return				플레이어가 놓은 돌의 종류와 같은 돌의 갯수
	 */
	public int getDown(int x, int y, int cnt_stone) {
		int cnt = 0; // 같은 돌의 갯수
		
		try {
			while(true) {
				if(int2d[++x][y] == cnt_stone) { // x가 인덱스 범위(10)를 넘을 수 있으므로 try-catch구문으로  exception처리
					cnt++;
				}else {
					break;
				}
			}			
		}catch(IndexOutOfBoundsException e) {
			System.out.println("line out");
		}
		
		return cnt;
	}
	/**
	 * 왼쪽 방향으로 같은 돌의 갯수를 카운팅 하는 메서드
	 * @param x		플레이어가 놓은 돌의 i좌표
	 * @param y		플레이어가 놓은 돌의 j좌표
	 * @param cnt_stone		플레이어가 놓은 돌의 종류
	 * @return				플레이어가 놓은 돌의 종류와 같은 돌의 갯수
	 */
	public int getLeft(int x, int y, int cnt_stone) {
		int cnt = 0;
		try {
			while(true) {
				if(int2d[x][--y] == cnt_stone) { // y가 음수값이 되면 안되므로 try-catch구문으로 exception 처리
					cnt++;
				}else {
					break;
				}
			}			
		}catch(IndexOutOfBoundsException e) {
			System.out.println("line out");
		}
		
		return cnt;
	}
	/**
	 * 오른쪽 방향으로 같은 돌의 갯수를 카운팅 하는 메서드
	 * @param x		플레이어가 놓은 돌의 i좌표
	 * @param y		플레이어가 놓은 돌의 j좌표
	 * @param cnt_stone		플레이어가 놓은 돌의 종류
	 * @return				플레이어가 놓은 돌의 종류와 같은 돌의 갯수
	 */
	public int getRight(int x, int y, int cnt_stone) {
		int cnt = 0;
		try {
			while(true) {
				if(int2d[x][++y] == cnt_stone) { // y값이 인덱스 범위(10)를 넘을 수 있으므로 try-catch구문으로 exception처리
					cnt++;
				}else {
					break;
				}
			}			
		}catch(IndexOutOfBoundsException e) {
			System.out.println("line out");
		}
		
		return cnt;
	}
	/**
	 * 왼쪽 위 방향으로 같은 돌의 갯수를 카운팅 하는 메서드
	 * @param x		플레이어가 놓은 돌의 i좌표
	 * @param y		플레이어가 놓은 돌의 j좌표
	 * @param cnt_stone		플레이어가 놓은 돌의 종류
	 * @return				플레이어가 놓은 돌의 종류와 같은 돌의 갯수
	 */
	public int getUpLe(int x, int y, int cnt_stone) {
		int cnt = 0;
		//숙제
		try {
			while(true) {
				if(int2d[--x][--y] == cnt_stone) { // x와 y가 음수값이 나올 수 있으므로  exception처리
					cnt++;
				}else {
					break;
				}
			}
		}catch(IndexOutOfBoundsException e) {
			System.out.println("line out");
		}
		
		return cnt;			
	}
	/**
	 * 오른쪽 위 방향으로 같은 돌의 갯수를 카운팅 하는 메서드
	 * @param x		플레이어가 놓은 돌의 i좌표
	 * @param y		플레이어가 놓은 돌의 j좌표
	 * @param cnt_stone		플레이어가 놓은 돌의 종류
	 * @return				플레이어가 놓은 돌의 종류와 같은 돌의 갯수
	 */
	public int getUpRi(int x, int y, int cnt_stone) {
		int cnt = 0;
		//숙제
		try {
			while(true) {
				if(int2d[--x][++y] == cnt_stone) { // x값이 음수값이 되거나 y값이 인덱스 범위를 넘어설 수 있으므로 exception처리
					cnt++;
				}else {
					break;
				}
			}
		}catch(IndexOutOfBoundsException e) {
			System.out.println("line out");
		}
		
		return cnt;			
	}
	/**
	 * 왼쪽 아래 방향으로 같은 돌의 갯수를 카운팅 하는 메서드
	 * @param x		플레이어가 놓은 돌의 i좌표
	 * @param y		플레이어가 놓은 돌의 j좌표
	 * @param cnt_stone		플레이어가 놓은 돌의 종류
	 * @return				플레이어가 놓은 돌의 종류와 같은 돌의 갯수
	 */
	public int getdwLe(int x, int y, int cnt_stone) {
		int cnt = 0; // 같은 돌의 갯수
		
		try {
			while(true) {
				if(int2d[++x][--y] == cnt_stone) { // y값이 음수값이 되거나 x값이 인덱스 범위를 넘어설 수 있으므로 exception처리
					cnt++;
				}else {
					break;
				}
			}			
		}catch(IndexOutOfBoundsException e) {
			System.out.println("line out");
		}
		
		return cnt;
	}
	/**
	 * 오른쪽 아래 방향으로 같은 돌의 갯수를 카운팅 하는 메서드
	 * @param x		플레이어가 놓은 돌의 i좌표
	 * @param y		플레이어가 놓은 돌의 j좌표
	 * @param cnt_stone		플레이어가 놓은 돌의 종류
	 * @return				플레이어가 놓은 돌의 종류와 같은 돌의 갯수
	 */
	public int getdwRi(int x, int y, int cnt_stone) {
		int cnt = 0; // 같은 돌의 갯수
		
		try {
			while(true) {
				if(int2d[++x][++y] == cnt_stone) {
					cnt++;
				}else {
					break;
				}
			}			
		}catch(IndexOutOfBoundsException e) {
			System.out.println("line out");
		}
		
		return cnt;
	}
	
	
	
	
	
	
	
}
