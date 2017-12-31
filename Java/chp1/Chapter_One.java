
public class Chapter_One {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		System.out.println(isUnique("hello"));
		System.out.println(isUnique("world "));
	}
	
	static boolean isUnique(String str) {
		// need to verify ASCII vs. Unicode
		
		//create array of bool values for 256 vals
		boolean[] boolVal = new boolean[256];
		for (int i = 0; i < str.length(); i++) {
			char charVal = str.charAt(i);
			// check if val exists; return false if so
			if (boolVal[charVal]) {
				return false;
			} else {
				boolVal[charVal] = true;
			}
		}
		//after going through string check 
		return true; 
				
	}

}
