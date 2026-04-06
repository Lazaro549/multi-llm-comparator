type Props = {
  model: string;
  response: string;
};

export default function ResponseCard({ model, response }: Props) {
  return (
    <div
      style={{
        flex: 1,
        border: "1px solid #ccc",
        padding: 12,
        borderRadius: 10,
      }}
    >
      <h3>{model}</h3>
      <p>{response}</p>
    </div>
  );
}
