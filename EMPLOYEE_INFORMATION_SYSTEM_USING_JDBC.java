package JDBC;

import java.sql.*;
import java.io.*;

public class JDBC {
    void insert() {
        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            Class.forName("sun.jdbc.odbc.JdbcOdbcDriver");
            Connection con = DriverManager.getConnection("jdbc:odbc:stud21", "system", "admin");
            PreparedStatement pst = con.prepareStatement("insert into stud21 values(?,?,?)");

            System.out.println("Enter the studId");
            int a = Integer.parseInt(br.readLine());
            System.out.println("Enter the studName");
            String b = br.readLine();
            System.out.println("Enter the Department");
            String c = (br.readLine());

            pst.setInt(1, a);
            pst.setString(2, b);
            pst.setString(3, c);
            pst.executeUpdate();
            System.out.println("Record Inserted");
            pst.close();
        } catch (Exception e) {
            System.out.println("Error" + e);
        }
    }

    void select() {
        int x;
        String y, z;
        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            Class.forName("sun.jdbc.odbc.JdbcOdbcDriver");
            Connection con = DriverManager.getConnection("jdbc:odbc:stud21", "system", "admin");
            PreparedStatement pst = con.prepareStatement("select * from stud21 where stdid=?");

            System.out.println("students details");
            System.out.println("Enter studid");
            int a = Integer.parseInt(br.readLine());
            pst.setInt(1, a);
            ResultSet rs = pst.executeQuery();

            System.out.println("studid\t\tstudname\t\tdept");
            while (rs.next()) {
                x = rs.getInt(1);
                y = rs.getString(2);
                z = rs.getString(3);
                System.out.println(x + "\t\t" + y + "\t\t" + z);
            }
        } catch (Exception e) {
            System.out.println("Error" + e);
        }
    }

    public static void main(String arg[]) throws IOException {
        JDBC db = new JDBC();
        char f;
        int ch;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("students details");
        do {
            System.out.println("\n1.insert\n2.Select\n3.exit");
            System.out.println("enter your choice");
            ch = Integer.parseInt(br.readLine());
            switch (ch) {
                case 1:
                    db.insert();
                    break;
                case 2:
                    db.select();
                    break;
                default:
                    System.out.println("your choice is wrong");
                    break;
            }
            System.out.println("Do u want to continue(y/n)");
            f = br.readLine().charAt(0);
        } while (f == 'y' || f == 'Y');
    }
}
