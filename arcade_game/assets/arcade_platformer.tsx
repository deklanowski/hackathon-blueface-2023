<?xml version="1.0" encoding="UTF-8"?>
<tileset version="1.10" tiledversion="1.10.1" name="arcade_platformer" tilewidth="128" tileheight="128" tilecount="63" columns="0">
 <editorsettings>
  <export target="arcade_platformer.tsx" format="tsx"/>
 </editorsettings>
 <grid orientation="orthogonal" width="1" height="1"/>
 <tile id="0">
  <image width="128" height="128" source="images/ground/Grass/grass.png"/>
 </tile>
 <tile id="1">
  <image width="128" height="128" source="images/ground/Grass/grassCenter_round.png"/>
 </tile>
 <tile id="2">
  <image width="128" height="128" source="images/ground/Grass/grassCenter.png"/>
 </tile>
 <tile id="3">
  <image width="128" height="128" source="images/ground/Grass/grassCliff_left.png"/>
 </tile>
 <tile id="4">
  <image width="128" height="128" source="images/ground/Grass/grassCliff_right.png"/>
 </tile>
 <tile id="5">
  <image width="128" height="128" source="images/ground/Grass/grassCliffAlt_left.png"/>
 </tile>
 <tile id="6">
  <image width="128" height="128" source="images/ground/Grass/grassCliffAlt_right.png"/>
 </tile>
 <tile id="7">
  <image width="128" height="128" source="images/ground/Grass/grassCorner_left.png"/>
 </tile>
 <tile id="8">
  <image width="128" height="128" source="images/ground/Grass/grassCorner_right.png"/>
 </tile>
 <tile id="9">
  <image width="128" height="128" source="images/ground/Grass/grassHalf_left.png"/>
 </tile>
 <tile id="10">
  <image width="128" height="128" source="images/ground/Grass/grassHalf_mid.png"/>
 </tile>
 <tile id="11">
  <image width="128" height="128" source="images/ground/Grass/grassHalf_right.png"/>
 </tile>
 <tile id="12">
  <image width="128" height="128" source="images/ground/Grass/grassHalf.png"/>
 </tile>
 <tile id="13">
  <image width="128" height="128" source="images/ground/Grass/grassHill_left.png"/>
  <objectgroup draworder="index">
   <object id="2" x="0.545455" y="0.909091">
    <polygon points="-0.545455,-0.909091 127.455,127.091 -0.545455,127.091"/>
   </object>
  </objectgroup>
 </tile>
 <tile id="14">
  <image width="128" height="128" source="images/ground/Grass/grassHill_right.png"/>
  <objectgroup draworder="index">
   <object id="1" x="0" y="128">
    <polygon points="0,0 128,0 128,-128"/>
   </object>
  </objectgroup>
 </tile>
 <tile id="15">
  <image width="128" height="128" source="images/ground/Grass/grassLeft.png"/>
 </tile>
 <tile id="16">
  <image width="128" height="128" source="images/ground/Grass/grassMid.png"/>
 </tile>
 <tile id="17">
  <image width="128" height="128" source="images/ground/Grass/grassRight.png"/>
 </tile>
 <tile id="29">
  <image width="128" height="128" source="images/HUD/hudHeart_empty.png"/>
 </tile>
 <tile id="30">
  <image width="128" height="128" source="images/HUD/hudHeart_full.png"/>
 </tile>
 <tile id="33">
  <image width="128" height="128" source="images/HUD/hudJewel_blue.png"/>
 </tile>
 <tile id="35">
  <image width="128" height="128" source="images/HUD/hudJewel_green.png"/>
 </tile>
 <tile id="37">
  <image width="128" height="128" source="images/HUD/hudJewel_red.png"/>
 </tile>
 <tile id="39">
  <image width="128" height="128" source="images/HUD/hudJewel_yellow.png"/>
 </tile>
 <tile id="41">
  <image width="128" height="128" source="images/HUD/hudKey_blue.png"/>
 </tile>
 <tile id="43">
  <image width="128" height="128" source="images/HUD/hudKey_green.png"/>
 </tile>
 <tile id="45">
  <image width="128" height="128" source="images/HUD/hudKey_red.png"/>
 </tile>
 <tile id="47">
  <image width="128" height="128" source="images/HUD/hudKey_yellow.png"/>
 </tile>
 <tile id="53">
  <image width="128" height="128" source="images/HUD/hudX.png"/>
 </tile>
 <tile id="54">
  <properties>
   <property name="point_value" type="int" value="5"/>
  </properties>
  <image width="128" height="128" source="images/items/polyBox.png"/>
 </tile>
 <tile id="55">
  <properties>
   <property name="point_value" type="int" value="20"/>
  </properties>
  <image width="128" height="128" source="images/items/polyphonebox.png"/>
 </tile>
 <tile id="56">
  <properties>
   <property name="point_value" type="int" value="10"/>
  </properties>
  <image width="128" height="128" source="images/items/polyheadset.png"/>
 </tile>
 <tile id="60">
  <image width="128" height="128" source="images/items/flagGreen_down.png"/>
 </tile>
 <tile id="61">
  <image width="128" height="128" source="images/items/flagGreen1.png"/>
  <animation>
   <frame tileid="61" duration="250"/>
   <frame tileid="62" duration="250"/>
  </animation>
 </tile>
 <tile id="62">
  <image width="128" height="128" source="images/items/flagGreen2.png"/>
 </tile>
 <tile id="69">
  <image width="128" height="128" source="images/items/gemBlue.png"/>
 </tile>
 <tile id="70">
  <image width="128" height="128" source="images/items/gemGreen.png"/>
 </tile>
 <tile id="71">
  <image width="128" height="128" source="images/items/gemRed.png"/>
 </tile>
 <tile id="72">
  <image width="128" height="128" source="images/items/gemYellow.png"/>
 </tile>
 <tile id="77">
  <image width="128" height="128" source="images/items/star.png"/>
 </tile>
 <tile id="84">
  <image width="128" height="128" source="images/tiles/office-desk.png"/>
 </tile>
 <tile id="95">
  <image width="128" height="128" source="images/tiles/brickBrown.png"/>
 </tile>
 <tile id="96">
  <image width="128" height="128" source="images/tiles/brickGrey.png"/>
 </tile>
 <tile id="104">
  <image width="128" height="128" source="images/tiles/doorOpen_mid.png"/>
 </tile>
 <tile id="105">
  <image width="128" height="128" source="images/tiles/doorOpen_top.png"/>
 </tile>
 <tile id="106">
  <image width="128" height="128" source="images/tiles/fence.png"/>
 </tile>
 <tile id="107">
  <image width="128" height="128" source="images/tiles/fenceBroken.png"/>
 </tile>
 <tile id="108">
  <image width="128" height="128" source="images/tiles/grass.png"/>
 </tile>
 <tile id="109">
  <image width="128" height="128" source="images/tiles/ladderMid.png"/>
 </tile>
 <tile id="110">
  <image width="128" height="128" source="images/tiles/ladderTop.png"/>
 </tile>
 <tile id="111">
  <image width="128" height="128" source="images/tiles/lava.png"/>
 </tile>
 <tile id="112">
  <image width="128" height="128" source="images/tiles/lavaTop_high.png"/>
 </tile>
 <tile id="113">
  <image width="128" height="128" source="images/tiles/lavaTop_low.png"/>
 </tile>
 <tile id="126">
  <image width="128" height="128" source="images/tiles/signExit.png"/>
 </tile>
 <tile id="127">
  <image width="128" height="128" source="images/tiles/signLeft.png"/>
 </tile>
 <tile id="128">
  <image width="128" height="128" source="images/tiles/signRight.png"/>
 </tile>
 <tile id="141">
  <image width="128" height="128" source="images/tiles/torch1.png"/>
 </tile>
 <tile id="142">
  <image width="128" height="128" source="images/tiles/torch2.png"/>
  <animation>
   <frame tileid="141" duration="250"/>
   <frame tileid="142" duration="250"/>
  </animation>
 </tile>
 <tile id="144">
  <image width="128" height="128" source="images/tiles/water.png"/>
 </tile>
 <tile id="145">
  <image width="128" height="128" source="images/tiles/waterTop_high.png"/>
 </tile>
 <tile id="146">
  <image width="128" height="128" source="images/tiles/waterTop_low.png"/>
 </tile>
 <tile id="150">
  <image width="128" height="128" source="images/tiles/grass2.png"/>
  <animation>
   <frame tileid="108" duration="250"/>
   <frame tileid="150" duration="250"/>
  </animation>
 </tile>
 <tile id="151">
  <image width="66" height="92" source="images/items/alienPink.png"/>
 </tile>
</tileset>
