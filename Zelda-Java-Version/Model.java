//Ethan Potts
//CSCE 3193 Assignment 5
//03-31-2023
//Assignment Description: This Assignment creates a map editor for our game. It uses keyboard inputs to move around the
//map and mouse inputs to place and remove tiles.
//Model.java handles the locations and placement of tiles on the map.

import java.util.ArrayList;
import java.util.Iterator;


class Model
{
	ArrayList<Sprite> sprites; //Holds tiles active on the screem
	Link link;
	View v;
	

	Model()
	{
		sprites = new ArrayList<Sprite>();
		this.link = new Link(100,100);
		sprites.add(this.link);
	}

	public void unmarshal(Json ob) //loads the map from map.json
	{
		//sprites = new ArrayList<Sprite>();
		Json tmpList = ob.get("tiles");
		for(int i = 0; i < tmpList.size(); i++)
    		sprites.add(new Tile(tmpList.get(i)));
		tmpList = ob.get("pots");
		for(int i = 0; i < tmpList.size(); i++)
    		sprites.add(new Pot(tmpList.get(i)));

	}

	public void update() //unused atm
	{

		if(sprites != null)
		{
			
			Iterator<Sprite> it = sprites.iterator();
		
			while(it.hasNext())
			{
				Sprite temp1 = it.next();
				

				Iterator<Sprite> itIN = sprites.iterator();
				while(itIN.hasNext())
				{
					Sprite temp2 = itIN.next();
					if(temp1.collisionDetector1(temp2))
					{
						if(temp1.whatAmI("LINK") && temp2.whatAmI("TILE"))
						{
							link.x = link.prevX;
							link.y = link.prevY;
						}
						if(temp2.whatAmI("BOOMER") && (temp1.whatAmI("TILE") || temp1.whatAmI("POT")))
						{
							((Boomerang)temp2).isActive = false;
						}
						if(temp2.whatAmI("BOOMER") && temp1.whatAmI("POT"))
						{
							((Pot)temp1).isBroke = true;
						}
						if(temp2.whatAmI("POT") && temp1.whatAmI("LINK"))
						{
							((Pot)temp2).sendPot(link.direction);
						}
						if(temp2.whatAmI("POT") && temp1.whatAmI("TILE"))
						{
							((Pot)temp2).isBroke = true;
						}
					}
					
				}
				temp1.update();
				if(temp1.whatAmI("BOOMER"))
				{
					if(((Boomerang)temp1).isActive == false)
					{
						it.remove();
					}
				}
				if(temp1.whatAmI("POT"))
				{
					if(((Pot)temp1).framesLeft <= 0)
					{
						it.remove();
					}
				}
		
				
			}
		}
		//);
		
		link.setPrevious();
		return;
	}

	

	public void setView(View view)
	{
		v = view;
		return;
	}

	public void placeTile(int x, int y) // places tile in tiles if there is not a tile at the clicked location. if not removes it
	{
		
		Iterator<Sprite> it = sprites.iterator();
		while(it.hasNext())
		{
			Sprite temp = it.next();
			
			if(temp.whatAmI("TILE"))
			{
				Tile tempTile = (Tile)temp;
				if(tempTile.tileThere(x,y))
				{
					it.remove();
					return;
				}
			}
		}

		Tile tNew = new Tile(x-x%50,y-y%50); // if it checks all tiles and there is none, place tile
		sprites.add(tNew);
	
	}

	public void placePot(int x, int y) // places tile in tiles if there is not a tile at the clicked location. if not removes it
	{
		
		Iterator<Sprite> it = sprites.iterator();
		while(it.hasNext())
		{
			Sprite temp = it.next();
			
			if(temp.whatAmI("TILE"))
			{
				Tile tempTile = (Tile)temp;
				if(tempTile.tileThere(x,y))
				{
					return;
				}
			}
		}

		Pot pNew = new Pot(x-x%50,y-y%50); // if it checks all tiles and there is none, place tile
		sprites.add(pNew);
	
	}

	public void sendBoomerang()
	{
		Boomerang boom = new Boomerang(link.x+link.w/2, link.y+link.h/2, link.direction);
		sprites.add(boom);
	}

	public Json marshal() // saves tile objects and locations into map.json
	{
		Json ob = Json.newObject();
		Json tileList = Json.newList();
		Json potList = Json.newList();
		ob.add("tiles", tileList);
		ob.add("pots",potList);
		for(int i = 0; i < sprites.size(); i++)
		{
			if(sprites.get(i).whatAmI("TILE"))
			{
        		tileList.add(((Tile)sprites.get(i)).marshal());
			}
			if(sprites.get(i).whatAmI("POT"))
			{
        		potList.add(((Pot)sprites.get(i)).marshal());
			}
		}


        return ob;
	}

	

}