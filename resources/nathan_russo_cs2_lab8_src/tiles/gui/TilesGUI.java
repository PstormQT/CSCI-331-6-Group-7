package tiles.gui;

import java.util.List;
import javafx.application.Application;
import javafx.application.Platform;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.scene.paint.Color;
import javafx.scene.text.Font;
import javafx.stage.Stage;
import tiles.model.Direction;
import tiles.model.Observer;
import tiles.model.TilesModel;

public class TilesGUI extends Application implements Observer<TilesModel, String> {
    /** This declares the model */
    private TilesModel model;

    // This declares a border pane for all other game components.
    private BorderPane gameScreen;

    /** This declares the grid pane that will display the number titles. */
    private GridPane grid;

    // This creates the labels that will be displayed in the statistics box.
    // The actual values that correspond to these will be added separately.
    private final Label moves = new Label();
    private final Label status = new Label();
    private final Label score = new Label();
    private final Label bestScore = new Label();


    /** This updates the player's statistics above the board.
     */
    private void updateStatistics(){
        moves.setText("Moves: \n" + model.getMovesMade());
        status.setText("Status: \n" + model.getGameStatus());
        score.setText("Score: \n" + model.getScore());
        bestScore.setText("Best score: \n" + model.getBestScore());
    }

    /** This creates the grid pane that will display the number titles.
     * This fills each cell with a label based upon the model.
     *
     * @return the created gridPane.
     */
    private GridPane makeGridPane(){
        // This creates the grid pane that will display the number titles.
        GridPane gridPane = new GridPane();
        gridPane.setGridLinesVisible(true);

        // This creates a label for each spot on the gird.
        for (int i = 0; i < 4; i++){
            for (int j = 0; j < 4; j++){
                // This creates a label with a dimensions of 90 based upon the model's board.
                // It is black, centered, and set to Arial font 20.
                int number = model.getContent(i, j);
                Label cellLabel = new Label(Integer.toString(number));
                cellLabel.setFont(Font.font("Arial", 20));
                cellLabel.setTextFill(Color.BLACK);
                cellLabel.setPrefSize(90, 90);
                cellLabel.setAlignment(Pos.CENTER);
                // This changes the label's background color based off of its number.
                switch (number){
                    case 2: cellLabel.setStyle("-fx-background-color: #eee4da");  break;
                    case 4: cellLabel.setStyle("-fx-background-color: #ede0c8");  break;
                    case 8: cellLabel.setStyle("-fx-background-color: #f2b179");  break;
                    case 16: cellLabel.setStyle("-fx-background-color: #f59563");  break;
                    case 32: cellLabel.setStyle("-fx-background-color: #f67c5f");  break;
                    case 64: cellLabel.setStyle("-fx-background-color: #f65e3b");  break;
                    case 128: cellLabel.setStyle("-fx-background-color: #edcf72");  break;
                    case 256: cellLabel.setStyle("-fx-background-color: #edcc61");  break;
                    case 512: cellLabel.setStyle("-fx-background-color: #edc850");  break;
                    case 1028: cellLabel.setStyle("-fx-background-color: #edc53f");  break;
                    case 2048: cellLabel.setStyle("-fx-background-color: #edc22e");  break;
                }

                // This adds the label to the gird.
                gridPane.add(cellLabel, j, i);
            }
        }
        return gridPane;
    }

    @Override
    public void init() {
        List<String> args = this.getParameters().getRaw();
        this.model = new TilesModel(args.getFirst());
        model.addObserver(this);
    }

    /**
     * Construct the layout for the game.
     *
     * @param primaryStage container (window) in which to render the GUI
     */
    @Override
    public void start(Stage primaryStage) {
        /*
         ********************************** OBJECT CREATION **********************************
         */

        // This initializes a border pane with dimensions of 500 for all other game components.
        gameScreen = new BorderPane();
        gameScreen.setPrefSize(500, 450);

        // This initializes the grid pane that will display the number titles.
        grid = makeGridPane();

        // This creates the box that will contain game statistics.
        HBox statistics = new HBox();
        statistics.setSpacing(75);
        statistics.setPrefHeight(75);
        statistics.setAlignment(Pos.CENTER);

        // This creates the labels that will be displayed in the statistics box.
        // The actual values that correspond to these will be added separately.
        updateStatistics();
        moves.setFont(Font.font("Arial", 15));
        status.setFont(Font.font("Arial", 15));
        score.setFont(Font.font("Arial", 15));
        bestScore.setFont(Font.font("Arial", 15));
        moves.setTextFill(Color.BLACK);
        status.setTextFill(Color.BLACK);
        score.setTextFill(Color.BLACK);
        bestScore.setTextFill(Color.BLACK);

        // This creates the box that will contain the buttons to play the game.
        VBox actions = new VBox();
        actions.setSpacing(100);
        actions.setPrefWidth(120);
        actions.setAlignment(Pos.TOP_CENTER);

        // This creates the grid pane where the 4 direction buttons will reside.
        GridPane buttonPad = new GridPane();

        // This creates the 4 buttons that move the used to move the tiles on the board.
        Button upButton = new Button("^");
        Button downButton = new Button("v");
        Button leftButton = new Button("<");
        Button rightButton = new Button(">");
        upButton.setPrefSize(40, 40);
        downButton.setPrefSize(40, 40);
        leftButton.setPrefSize(40, 40);
        rightButton.setPrefSize(40, 40);
        upButton.setFont(Font.font(19));
        downButton.setFont(Font.font(19));
        leftButton.setFont(Font.font(19));
        rightButton.setFont(Font.font(19));
        upButton.setTextFill(Color.BLACK);
        downButton.setTextFill(Color.BLACK);
        leftButton.setTextFill(Color.BLACK);
        rightButton.setTextFill(Color.BLACK);

        // This creates the button that restarts the game.
        Button newGameButton = new Button("New Game");
        newGameButton.setAlignment(Pos.CENTER);
        newGameButton.setTextFill(Color.BLACK);

        // This creates the box that will act as a buffer for the left side of the screen.
        VBox leftBuffer = new VBox();
        leftBuffer.setPrefWidth(15);
        leftBuffer.prefHeight(500);

        /*
         ********************************** USER INPUT **********************************
         */

        if (!model.isGameOver()){
            // This tells the model to update the board based on if a specific button is clicked.
            upButton.setOnAction(event -> model.move(Direction.NORTH));
            downButton.setOnAction(event -> model.move(Direction.SOUTH));
            leftButton.setOnAction(event -> model.move(Direction.WEST));
            rightButton.setOnAction(event -> model.move(Direction.EAST));
        }

        // This tells the model to start a new game if the new game button is clicked.
        newGameButton.setOnAction(event -> model.newGame());

        /*
         ********************************** OBJECT COMBINATION **********************************
         */

        // This adds the 4 direction buttons to the button pad.
        buttonPad.add(upButton, 1, 0);
        buttonPad.add(downButton, 1, 2);
        buttonPad.add(leftButton, 0, 1);
        buttonPad.add(rightButton, 2, 1);

        // This adds the game's statistics to the statistics HBox.
        statistics.getChildren().addAll(moves, status, score, bestScore);

        // This adds the new game button first and then the button pad to actions VBox.
        actions.getChildren().addAll(newGameButton, buttonPad);

        // This adds the statistics HBox, action VBox, and the game grid to the game screen.
        gameScreen.setTop(statistics);
        gameScreen.setRight(actions);
        gameScreen.setCenter(grid);
        gameScreen.setLeft(leftBuffer);

        // This give the stage a scene, sets the title, and tells the stage to display.
        primaryStage.setScene(new Scene(gameScreen));
        primaryStage.setTitle("2048 Tiles");
        primaryStage.show();
    }

    /**
     * Called by the model, model.TilesModel, whenever there is a state change
     * that needs to be updated by the GUI.
     *
     * @param model the TilesModel
     * @param message the status message sent by the model
     */
    @Override
    public void update(TilesModel model, String message) {
        if ( Platform.isFxApplicationThread() ) {
            // This changes the player's statistics.
            updateStatistics();

            // This initializes the updated grid pane that will display the number titles.
            grid = makeGridPane();
            gameScreen.setCenter(grid);
        }
    }

    /**
     * This method is called before the application shuts down.
     * It provides a convenient place to save any information about the game
     * before closing the application.
     */
    @Override
    public void stop() {
        model.shutdown();
    }

    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("Usage: TilesGUI <TEST|EASY|NORMAL>");
            System.exit(0);
        }
        Application.launch(args);
    }
}