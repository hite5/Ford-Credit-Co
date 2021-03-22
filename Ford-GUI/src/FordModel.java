import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class FordModel {
    private JButton submit;
    private JPanel mainPanel;
    private JLabel FordLogo;
    private JLabel modelLabel;
    private JTextField customerInput;
    private int answer;
    private String message;

    public FordModel() {
        submit.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    answer = Integer.parseInt(customerInput.getText());
                    if (answer % 3 == 0 && answer % 5 == 0) {
                        message = "MustangBronco";
                    } else if (answer % 3 == 0) {
                        message = "Mustang";
                    } else if (answer % 5 == 0) {
                        message = "Bronco";
                    } else {
                        message = customerInput.getText();
                    }
                    JOptionPane.showMessageDialog(null, message);
                } catch (NumberFormatException exp){
                    JOptionPane.showMessageDialog(null, "Not a valid input!");
                }
            }
        });
    }


    public static void main(String[] args) {
        JFrame frame = new JFrame("Ford Model Selector");
        frame.setContentPane(new FordModel().mainPanel);
        frame.setPreferredSize(new Dimension(320,155));
        frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        frame.pack();
        frame.setVisible(true);
    }

}
