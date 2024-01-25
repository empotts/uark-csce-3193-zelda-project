//Ethan Potts
//CSCE 3193 Assignment 5
//03-31-2023
//Assignment Description: This Assignment creates a map editor for our game. It uses keyboard inputs to move around the
//map and mouse inputs to place and remove tiles.
//Tile.java handles the map components used in our game. Each instance stores the location of the tile.

import java.awt.image.BufferedImage;
import javax.imageio.ImageIO;
import java.io.File;
import java.awt.Graphics;

public class Tile extends Sprite
{
    static BufferedImage tileImage = null;
    
    

    public Tile(int x, int y) //Tile Constructor with intial position
    {
        this.x = x;
        this.y = y;
        w = 50;
        h = 50;
        
        if(tileImage == null)
        {
            try //Imports png images
            {
                tileImage = ImageIO.read(new File("ImageFolder/tile.jpg"));
            }
            catch(Exception e) 
            {
                e.printStackTrace(System.err);
                System.exit(1);
            }
        }
        setTag("TILE");

    }

    public Tile(Json ob) // JSON Constructor from map.json
    {
        
        super((int)ob.getLong("tileX"),(int)ob.getLong("tileY"));
        try //Imports png images
		{
			tileImage = ImageIO.read(new File("ImageFolder/tile.jpg"));
		}
		catch(Exception e) 
		{
			e.printStackTrace(System.err);
			System.exit(1);
		}
        w = 50;
        h=50;
        setTag("TILE");
    }

    public boolean tileThere(int x, int y) // returns if a tile is at the location passed to the method
    {
        int roundX = x - x%w; // rounds to nearest tile
        int roundY = y - y%h;

        if(this.x == roundX && this.y == roundY)
        {
            return true;
        }

		return false;
    }

    public Json marshal() //saves tile to Json object
    {
        Json ob = Json.newObject();
        ob.add("tileX", this.x);
        ob.add("tileY", this.y);
        return ob;
    }

    public void update()
    {
        //IMPLEMENT
    }

    @Override
    public String toString()
    {
        return "Tile @" + x + "," + y ;
    }

    public void draw(Graphics g, int viewX, int viewY)
    {
        g.drawImage(Tile.tileImage, x-viewX, y-viewY, null);
    }
    public boolean whatAmI(String s)
	{
		return tag==s; //MAY NEED TO CHANGE
	}

    



    
}
