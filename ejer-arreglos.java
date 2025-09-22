import java.util.*;

public class Ventas {
    private String[] meses = {
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    };
    private String[] departamentos = {"Ropa", "Deportes", "Juguetería"};
    private int[][] ventas = new int[12][3];

    public void insertarVenta(String mes, String depto, int monto) {
        int iMes = Arrays.asList(meses).indexOf(mes);
        int iDepto = Arrays.asList(departamentos).indexOf(depto);
        ventas[iMes][iDepto] = monto;
    }

    public int buscarVenta(String mes, String depto) {
        int iMes = Arrays.asList(meses).indexOf(mes);
        int iDepto = Arrays.asList(departamentos).indexOf(depto);
        return ventas[iMes][iDepto];
    }

    public void eliminarVenta(String mes, String depto) {
        int iMes = Arrays.asList(meses).indexOf(mes);
        int iDepto = Arrays.asList(departamentos).indexOf(depto);
        ventas[iMes][iDepto] = 0;
    }

    public void imprimirTabla() {
        System.out.printf("%-12s%-12s%-12s%-12s%n", "Mes", "Ropa", "Deportes", "Juguetería");
        for (int i = 0; i < meses.length; i++) {
            System.out.printf("%-12s%-12d%-12d%-12d%n", 
                meses[i], ventas[i][0], ventas[i][1], ventas[i][2]);
        }
    }

    public static void main(String[] args) {
        Ventas v = new Ventas();
        v.insertarVenta("Enero", "Ropa", 1500);
        v.insertarVenta("Enero", "Deportes", 2000);
        v.insertarVenta("Febrero", "Juguetería", 3500);
        v.insertarVenta("Diciembre", "Ropa", 5000);

        System.out.println("\nTABLA DE VENTAS:");
        v.imprimirTabla();
    }
}
