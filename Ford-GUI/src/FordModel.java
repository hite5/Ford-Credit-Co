import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class FordModel {
    private JButton submit;
    private JPanel mainPanel;

    public FordModel() {
        submit.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {

            }
        });
    }


    public static void main(String[] args) {
        JFrame frame = new JFrame("Ford Model Selector");
        frame.setContentPane(new FordModel().mainPanel);
        frame.setPreferredSize(new Dimension(550,400));
        frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        frame.pack();
        frame.setVisible(true);
    }
}
