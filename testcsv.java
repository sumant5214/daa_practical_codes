import java.io.*;

class testcsv {
    public static void main(String args[]) {
        FileReader fr;
        BufferedReader br;
        String choicesStr[] = new String[5];
        int i, j, k, ctr, size, zeroInv, oneInv, twoInv, threeInv, threePlusInv, choices[] = {};
        String studChoice;
        zeroInv = oneInv = twoInv = threeInv = threePlusInv = 0;
        try {
            fr = new FileReader("./inversion.csv");
            br = new BufferedReader(fr);
            while ((studChoice = br.readLine()) != null) {
                ctr = 0;
                choicesStr = studChoice.split(",");
                choices = new int[choicesStr.length];
                if (choicesStr.length > 2) {
                    for (i = 0; i < choicesStr.length; i++) {
                        choices[i] = Integer.parseInt(choicesStr[i]);
                    }
                } else {

                    throw new NullPointerException();
                }
                for (j = 0; j < choices.length - 1; j++) {
                    for (k = j + 1; k < choices.length; k++) {
                        if (choices[j] > choices[k]) {
                            ctr++;
                        }
                    }
                }
                if (ctr == 0)
                    zeroInv++;
                else if (ctr == 1)
                    oneInv++;
                else if (ctr == 2)
                    twoInv++;
                else if (ctr == 3)
                    threeInv++;
                else
                    threePlusInv++;
            }
            System.out.println("Count of students with 0 inversion: " + zeroInv);
            System.out.println("Count of students with 1 inversion: " + oneInv);
            System.out.println("Count of students with 2 inversion: " + twoInv);
            System.out.println("Count of students with 3 inversion: " + threeInv);
            System.out.println("Count of students with more than 3 inversion: " + threePlusInv);
            br.close();
            fr.close();
        } catch (IOException ioe) {
            ioe.printStackTrace();
        }
    }
}