import javax.swing.*;

public class App {
    public static void main(String[] args) throws Exception {
        int width = 500;
        int height = 500;

        JFrame frame = new JFrame("Snake");
        frame.setVisible(true);
        frame.setSize(width, height);
        frame.setLocationRelativeTo(null);
        frame.setResizable(false);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        SnakeGame snakeGame = new SnakeGame(width, height);
        frame.add(snakeGame);
        frame.pack();
        snakeGame.requestFocus();
    }
}
