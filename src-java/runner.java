import helper.Lexer;
import helper.Stack;
import java.util.ArrayList;

public class runner {
    public static Lexer lexer = new Lexer("./test.jail");
    public static Stack stack = new Stack(256);
    public static ArrayList<String> programR = lexer.getProgram();
    public static int pc = 0;
    public static String opcodeR;
    public static void main(String[] args){
        while (!programR.get(pc).equals("halt")){
            opcodeR = programR.get(pc);
            pc++;
            if (opcodeR.equals("push")){
                stack.push(Integer.valueOf(programR.get(pc)));
                pc++;
            } else if (opcodeR.equals("print")){
                System.out.println(programR.get(pc));
                pc++;
            } else if (opcodeR.equals("add")){
                int a = stack.pop();
                int b = stack.pop();
                stack.push(a + b);
            } else if (opcodeR.equals("jump.eq.0")){
                int _num = stack.top();
                if (_num == 0){
                    pc = Integer.valueOf(lexer.getLabelCounter().get(programR.get(pc)));
                } else {
                    pc++;
                }
            }
        }
    }
}
