import java.nio.file.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        List<String> lines = Files.readAllLines(Paths.get("output.txt"));
        String[][] matrix = new String[lines.size()][];

        for (int i = 0; i < lines.size(); i++) {
            matrix[i] = lines.get(i).split(" ");
        }

        solve(matrix);
        System.out.println();
    }

    public static void solve(String[][] board) {

        int n = board.length;
        int m = board[0].length;

        // 1st row
        for(int i = 0; i < m; i++){
            if(board[0][i].equals(".")){
                dfs(board, 0, i);
            }
        }

        // last row
        for(int i = 0; i < m; i++){
            if(board[n - 1][i].equals(".")){
                dfs(board, n - 1, i);
            }
        }

        // 1st column
        for(int i = 0; i < n; i++){
            if(board[i][0].equals(".")){
                dfs(board, i, 0);
            }
        }

        // last column
        for(int i = 0; i < n; i++){
            if(board[i][m - 1].equals(".")){
                dfs(board, i, m - 1);
            }
        }


        int res = 0;

        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if(board[i][j].equals(".")){
                    res++;
                    board[i][j] = "I";
                }
            }
        }

        for (String[] row : board) {
            System.out.println(Arrays.toString(row));
        }

        System.out.println(res);
    }

    public static void dfs(String[][] grid, int row, int col){
        if(row < 0 || col < 0 || row >= grid.length || col >= grid[0].length || Character.isDigit(grid[row][col].charAt(0)) || grid[row][col].equals("X")){
            return;
        }

        grid[row][col] = "X";

        dfs(grid, row + 1, col);
        dfs(grid, row - 1, col);
        dfs(grid, row, col - 1);
        dfs(grid, row, col + 1);
        dfs(grid, row + 1, col + 1);
        dfs(grid, row - 1, col - 1);
        dfs(grid, row + 1, col - 1);
        dfs(grid, row - 1, col + 1);
    }
}