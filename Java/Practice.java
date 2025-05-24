import java.lang.Math;

public class Practice {
    public static void main(String args[]) {
        int num1 = 8;
        int num2 = 20;
       
        int ii[] = {1,2,3};

        int result = num1 + num2;
        System.out.println(result);
        System.out.print(ii);

        double numarray[] = new double[4];
        System.err.println(numarray);

        for(int i=0;i<4;i++) {
            numarray[i] = Math.random();
            System.out.println(i + " " + numarray[i]);
        }


        // Jagged Array
        int ar[][] = new int[3][];
        ar[0] = new int[10];
        ar[1] = new int[12];
        ar[2] = new int[2];
        for(int i=0;i< ar.length;i++) {
            for(int j=0;j<ar[i].length;j++) {
                ar[i][j] = (int) (Math.random() * 1000);
            }
        }

          for(int i=0;i< ar.length;i++) {
            for(int j=0;j<ar[i].length;j++) {
                System.out.print(ar[i][j] + " ");
            }
            System.out.println();
        }

        for(int[] arr: ar) {
            for(int a: arr) {
                System.out.print(a + "  ");
            }
        }
    }
}