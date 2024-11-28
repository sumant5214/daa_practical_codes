import java.io.*;

class empsal {
    public static void main(String[] args) {
        PrintWriter pw;
        BufferedReader br, brtemp;
        try {
            br = new BufferedReader(new FileReader("./emp.csv"));
            String line;
            String empdata[] = new String[8];
            Object objData[] = br.lines().toArray();
            for (int i = 0; i < objData.length; i++) {
                empdata = objData[i].toString().split(",");
                int baseSal = Integer.parseInt(empdata[3]);
                int bonus = Integer.parseInt(empdata[4]);

                int deductions = Integer.parseInt(empdata[5]);
                int grossSal = baseSal + bonus;
                int netSal = grossSal - deductions;
                line = objData[i].toString() + "," + grossSal + "," +

                        netSal;

                objData[i] = line;
            }
            File f = new File("./emp.csv");
            f.delete();
            objData = QuickSort.start(objData, 0, objData.length - 1);
            System.out.println("Employee with lowest salary is " +

                    objData[0].toString().split(",")[1] + " " +
                    objData[0].toString().split(",")[2] + " with salary " +
                    objData[0].toString().split(",")[3]);

            System.out.println("Employee with lowest salary is " +

                    objData[objData.length - 1].toString().split(",")[1] + " " +
                    objData[objData.length - 1].toString().split(",")[2] + " with salary " +
                    objData[objData.length - 1].toString().split(",")[3]);

            pw = new PrintWriter(new FileWriter("./emp.csv"), true);
            for (int j = 0; j < objData.length; j++) {
                pw.println(objData[j].toString());
            }
            pw.close();
            br.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}