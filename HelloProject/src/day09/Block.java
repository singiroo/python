package day09;

/**
 * ��Ʈ���� ������ ��Ÿ���� Ŭ����
 * ������ Ÿ��
 * �ش� ������ ����
 * ������ ������ ��ǥ ����
 * @author PC-25
 *
 */
public class Block {

	public int kind = 7 ;		//������  Ÿ�� (1 ~ 7). ���÷� 7�̶� ������ 
	public int status = 1;		//������ ����(������ ȸ���� ���). ���÷� �ϳ��� ����� 1�� ������
	public int i = 1;			//2���� �迭������ ������ �������� i��ǥ
	public int j = 5;			//2���� �迭������ ������ ������ j��ǥ
	
	@Override
	public String toString() {
		return "Block [kind=" + kind + ", status=" + status + ", i=" + i + ", j=" + j + "]";
	}
	

}