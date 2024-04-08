import React, { useCallback, useState } from "react";
import "./App.css";
import Calendar from "react-calendar";

type ValuePiece = Date | null;

type Value = ValuePiece | [ValuePiece, ValuePiece];

interface ListItemProps {
  value: number;
  index: number;
  onIncrement: (index: number) => void;
}

const ListItem: React.FC<ListItemProps> = React.memo(
  ({ value, index, onIncrement }) => {
    console.log(`Renderizando item ${value}`);

    return (
      <li>
        <p>Valor: {value}</p>
        <button
          onClick={() => {
            onIncrement(index);
          }}
        >
          Incrementar
        </button>
      </li>
    );
  }
);

const MyList: React.FC = () => {
  const [items, setItems] = useState<number[]>([1, 2, 3]);
  const [dummyState, setDummyState] = useState(false);

  const incrementItem = useCallback((index: number) => {
    const newItems = [...items];
    newItems[index] += 1;
    setItems(newItems);
  }, []);

  const forceRerender = () => {
    setDummyState(!dummyState);
  };

  return (
    <div>
      <button onClick={forceRerender}>Forçar Rerender</button>
      <ul>
        {items.map((item, index) => {
          return (
            <div>
              <ListItem
                onIncrement={incrementItem}
                value={item}
                index={index}
                key={index}
              />
            </div>
          );
        })}
      </ul>
    </div>
  );
};

function App() {
  const [value, onChange] = useState<Value>(new Date());

  console.log("value", value);

  return (
    <>
      <MyList />
      <div style={{ width: 300 }}>
        <Calendar
          onChange={onChange}
          value={value}
          selectRange
          returnValue="range"
        />
      </div>
    </>
  );
}

export default App;
