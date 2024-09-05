import java.io.File;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Scanner;

class Lexer{
    public static File mainfile = new File("./test.jail");
    public static ArrayList<String> program = new ArrayList<>();
    public static int lc = -1;
    public static HashMap<String, String> labelCounter = new HashMap<>();
    public static String[] curLine;
    public static String opcode = "";

    public static void readFile(){
        try {
            Scanner fileReader = new Scanner(mainfile);
            while(fileReader.hasNextLine()){
                lc++;
                curLine = fileReader.nextLine().split(" ");
                opcode = curLine[0].toLowerCase();
                if (opcode.endsWith(":")){
                    System.out.println("label");
                    labelCounter.put(opcode, Integer.toString(lc));
                    continue;
                } else if (opcode == ""){
                    continue;
                }
                program.add(opcode);
                System.out.println(opcode + ":");
                if (opcode.equals("push")){
                    // expect int next
                    System.out.println(opcode + ">>>>>");
                    String num = curLine[1];
                    program.add(num);
                    lc++;
                    continue;
                } else if (opcode.equals("print")){
                    // expect string next
                    System.out.println(opcode + ">>>>>");
                    String strL = String.join(" ", Arrays.copyOfRange(curLine, 1, curLine.length));
                    program.add(strL);
                    lc++;
                    continue;
                }
            }
            fileReader.close();
        } catch (Exception e){
            System.out.println(e.toString());
        }
    }

    public static void main(String[] args){
        readFile();
        String listString = String.join(", ", program);
        System.out.println(listString);
    }
}