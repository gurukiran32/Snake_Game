import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;
import java.util.Random;
import javax.swing.*;

public class SnakeGame extends JPanel implements ActionListener, KeyListener {
    private class Tile {
        int x, y;

        Tile(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    int width;
    int height;
    int tileSize = 20;

    // Snake
    Tile snakeHead;
    ArrayList<Tile> snakeBody;

    // Food
    Tile food;
    Random random;

    // game
    Timer gameLoop;
    int speedx, speedy;
    boolean gameOver = false;

    SnakeGame(int width, int height) {
        this.width = width;
        this.height = height;
        setPreferredSize(new Dimension(this.width, this.height));
        setBackground(Color.black);
        addKeyListener(this);
        setFocusable(true);

        snakeHead = new Tile(5, 5);
        snakeBody = new ArrayList<Tile>();

        food = new Tile(5, 5);
        random = new Random();
        placeFood();

        speedx = 0;
        speedy = 0;

        gameLoop = new Timer(100, this);
        gameLoop.start();

    }

    public void paint(Graphics g) {
        super.paint(g);
        draw(g);
    }

    public void draw(Graphics g) {

        // Grid
        // for (int i = 0; i < width / tileSize; i++) {
        // g.drawLine(i * tileSize, 0, i * tileSize, height);
        // g.drawLine(0, i * tileSize, width, i * tileSize);
        // }

        // Food
        g.setColor(Color.red);
        g.fillRect(food.x * tileSize, food.y * tileSize, tileSize, tileSize);

        // Snake head
        g.setColor(Color.green);
        g.fillRect(snakeHead.x * tileSize, snakeHead.y * tileSize, tileSize, tileSize);

        // snake body
        for (int i = 0; i < snakeBody.size(); i++) {
            Tile bodyPart = snakeBody.get(i);
            g.fillRect(bodyPart.x * tileSize, bodyPart.y * tileSize, tileSize, tileSize);
        }

        // score
        g.setFont(new Font("Arial", Font.PLAIN, 16));
        if (gameOver) {
            g.setColor(Color.red);
            g.drawString("Game Over: " + String.valueOf(snakeBody.size()), tileSize - 16, tileSize);

        } else {
            g.drawString("Score: " + String.valueOf(snakeBody.size()), tileSize - 16, tileSize);
        }
    }

    public void placeFood() {
        food.x = random.nextInt(width / tileSize);
        food.y = random.nextInt(height / tileSize);
    }

    public boolean collision(Tile tile1, Tile tile2) {
        return tile1.x == tile2.x && tile1.y == tile2.y;
    }

    public void move() {
        // eat food
        if (collision(snakeHead, food)) {
            snakeBody.add(new Tile(food.x, food.y));
            placeFood();
        }

        // snake body
        for (int i = snakeBody.size() - 1; i >= 0; i--) {
            Tile thisPart = snakeBody.get(i);
            if (i == 0) {
                thisPart.x = snakeHead.x;
                thisPart.y = snakeHead.y;
            } else {
                Tile prevPart = snakeBody.get(i - 1);
                thisPart.x = prevPart.x;
                thisPart.y = prevPart.y;
            }
        }

        // Snake head
        snakeHead.x += speedx;
        snakeHead.y += speedy;

        // game over
        for (int i = 0; i < snakeBody.size(); i++) {
            Tile snakePart = snakeBody.get(i);
            if (collision(snakeHead, snakePart)) {
                gameOver = true;
            }

            if (snakeHead.x * tileSize < 0 || snakeHead.x * tileSize > width ||
                    snakeHead.y * tileSize < 0 || snakeHead.y * tileSize > height) {
                gameOver = true;
            }
        }

    }

    @Override
    public void actionPerformed(ActionEvent e) {
        move();
        repaint();
        if (gameOver) {
            gameLoop.stop();
        }
    }

    @Override
    public void keyPressed(KeyEvent e) {
        if (e.getKeyCode() == KeyEvent.VK_UP && speedy != 1) {
            speedx = 0;
            speedy = -1;
        } else if (e.getKeyCode() == KeyEvent.VK_DOWN && speedy != -1) {
            speedx = 0;
            speedy = 1;
        } else if (e.getKeyCode() == KeyEvent.VK_LEFT && speedx != 1) {
            speedx = -1;
            speedy = 0;
        } else if (e.getKeyCode() == KeyEvent.VK_RIGHT && speedx != -1) {
            speedx = 1;
            speedy = 0;
        }
    }

    // No use
    @Override
    public void keyTyped(KeyEvent e) {
    }

    // No use
    @Override
    public void keyReleased(KeyEvent e) {
    }

}
